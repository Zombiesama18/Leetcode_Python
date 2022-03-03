"""
2016. 增量元素之间的最大差值
给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，
其中 0 <= i < j < n 且 nums[i] < nums[j] 。
返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。
"""
from typing import *


def maximumDifference(nums: List[int]) -> int:
    minValue = nums[0]
    result = float('-INF')
    for i in range(1, len(nums)):
        if nums[i] > minValue:
            result = max(result, nums[i] - minValue)
        else:
            minValue = nums[i]
    if result == float('-INF'):
        result = -1
    return result



