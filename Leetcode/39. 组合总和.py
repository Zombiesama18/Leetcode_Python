# 39. 组合总和
# 给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
# candidates中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括target）都是正整数。
# 解集不能包含重复的组合。


def combinationSum(candidates, target):
    candidates.sort()
    output = []
    sub_output = []

    def recursion(num, candidates):
        for i in candidates:
            if num - i > 0:
                sub_output.append(i)
                recursion(num - i, candidates)
                sub_output.pop(-1)
            elif num - i == 0:
                sub_output.append(i)
                output.append(sub_output.copy())
                # append相当于引用，所以需要copy()
                sub_output.pop(-1)
                return
            else:
                return

    recursion(target, candidates)
    result = []
    for i in output:
        i.sort()
        if i not in result:
            result.append(i)
    return result


# 如果list是多维，不能用list(set())去重


candidates = [2, 3, 5]
target = 8
combinationSum(candidates, target)
