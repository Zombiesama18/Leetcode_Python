"""
6041. 多个数组求交集
给你一个二维整数数组 nums ，其中 nums[i] 是由 不同 正整数组成的一个非空数组，按 升序排列 返回一个数组，
数组中的每个元素在 nums 所有数组 中都出现过。
"""
from typing import List


def intersection(nums: List[List[int]]) -> List[int]:
    if len(nums) == 1:
        return list(sorted(nums[0]))
    unionSet = set(nums[0]).intersection(set(nums[1]))
    for i in range(2, len(nums)):
        unionSet.intersection_update(set(nums[i]))
    return list(sorted(unionSet))
