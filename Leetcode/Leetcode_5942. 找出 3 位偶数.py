"""
5942. 找出 3 位偶数
给你一个整数数组 digits ，其中每个元素是一个数字（0 - 9）。数组中可能存在重复元素。
你需要找出 所有 满足下述条件且 互不相同 的整数：
该整数由 digits 中的三个元素按 任意 顺序 依次连接 组成。
该整数不含 前导零
该整数是一个 偶数
例如，给定的 digits 是 [1, 2, 3] ，整数 132 和 312 满足上面列出的全部条件。
将找出的所有互不相同的整数按 递增顺序 排列，并以数组形式返回。
"""
import itertools


def findEvenNumbers(digits: [int]) -> [int]:
    def is_valid(num):
        return num[0] != 0 and num[2] % 2 == 0

    combs = itertools.permutations(digits, 3)
    result = set()
    for comb in combs:
        if is_valid(comb):
            result.add(100 * comb[0] + 10 * comb[1] + comb[2])
    result = list(result)
    result.sort()
    return result


