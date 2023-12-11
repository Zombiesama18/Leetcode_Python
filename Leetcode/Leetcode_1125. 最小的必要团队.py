"""
1125. 最小的必要团队

作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」
（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。
所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。
可以用每个人的编号来表示团队中的成员：
例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。
"""
from typing import List


def smallestSufficientTeam_BRUTEFORCE(req_skills: List[str], people: List[List[str]]) -> List[int]:
    req_skills = {skill: i for i, skill in enumerate(req_skills)}
    req_skill_set = set(req_skills.keys())
    result = [i for i in range(len(people))]

    def helper(index: int, current_skills: set, current_people: list):
        require_skills = req_skill_set.difference(current_skills)
        if not require_skills:
            nonlocal result
            if len(current_people) < len(result):
                result = current_people
        else:
            for i in range(index + 1, len(people)):
                for skill in people[i]:
                    if skill in require_skills:
                        temp_set = current_skills.copy()
                        temp_set.update(set(people[i]))
                        helper(i, temp_set, current_people + [i])
        return

    helper(-1, set(), [])
    return result


def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    skill_index = {s:i for i, s in enumerate(req_skills)}
    dp = [None] * (1 << len(req_skills))
    dp[0] = []
    for i, person in enumerate(people):
        cur_skill = 0
        for skill in person:
            cur_skill |= 1 << skill_index[skill]
        for prev in range(1 << len(req_skills)):
            if dp[prev] is None:
                continue
            comb = prev | cur_skill
            if dp[comb] is None or len(dp[comb]) > len(dp[prev]) + 1:
                dp[comb] = dp[prev] + [i]
    return dp[-1]
