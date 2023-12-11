"""
5996. 统计数组中相等且可以被整除的数对
给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 k ，
请你返回满足 0 <= i < j < n ，nums[i] == nums[j] 且 (i * j) 能被 k 整除的数对 (i, j) 的 数目 。
"""
import collections
from typing import *


def countPairs(nums: List[int], k: int) -> int:
    dictionary = collections.defaultdict(list)
    for i in range(len(nums)):
        dictionary[nums[i]].append(i)
    result = 0
    for num in dictionary:
        for i in range(len(dictionary[num]) - 1):
            for j in range(i + 1, len(dictionary[num])):
                if (dictionary[num][i] * dictionary[num][j]) % k == 0:
                    result += 1
    return result

