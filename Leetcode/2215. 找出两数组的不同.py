"""
2215. 找出两数组的不同
给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，请你返回一个长度为 2 的列表 answer ，其中：
answer[0] 是 nums1 中所有 不 存在于 nums2 中的 不同 整数组成的列表。
answer[1] 是 nums2 中所有 不 存在于 nums1 中的 不同 整数组成的列表。
注意：列表中的整数可以按 任意 顺序返回。
"""
from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    result1, result2 = [], []
    for num in nums1:
        if num not in nums2:
            result1.append(num)
    for num in nums2:
        if num not in nums1:
            result2.append(num)
    return [result1, result2]
