"""
2206. 将数组划分成相等数对
给你一个整数数组 nums ，它包含 2 * n 个整数。
你需要将 nums 划分成 n 个数对，满足：
每个元素 只属于一个 数对。
同一数对中的元素 相等 。
如果可以将 nums 划分成 n 个数对，请你返回 true ，否则返回 false 。
"""
import collections
from typing import List


def divideArray(nums: List[int]) -> bool:
    numDict = collections.Counter(nums)
    for num in numDict:
        if numDict[num] % 2 != 0:
            return False
    return True

