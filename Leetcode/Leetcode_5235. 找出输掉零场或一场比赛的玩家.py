"""
5235. 找出输掉零场或一场比赛的玩家
给你一个整数数组 matches 其中 matches[i] = [winneri, loseri] 表示在一场比赛中 winneri 击败了 loseri 。
返回一个长度为 2 的列表 answer ：
answer[0] 是所有 没有 输掉任何比赛的玩家列表。
answer[1] 是所有恰好输掉 一场 比赛的玩家列表。
两个列表中的值都应该按 递增 顺序返回。
注意：
只考虑那些参与 至少一场 比赛的玩家。
生成的测试用例保证 不存在 两场比赛结果 相同 。
"""
import collections
from typing import List


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    players = set()
    loseTimes = collections.defaultdict(int)
    for winner, loser in matches:
        players.add(winner)
        players.add(loser)
        loseTimes[loser] += 1
    return [list(sorted([player for player in players if loseTimes[player] == 0])),
            list(sorted([player for player in players if loseTimes[player] == 1]))]

