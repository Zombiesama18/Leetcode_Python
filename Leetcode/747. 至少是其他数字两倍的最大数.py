"""
747. 至少是其他数字两倍的最大数
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。
请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。
"""
from typing import List


def dominantIndex(nums: List[int]) -> int:
    another = nums[:]
    another.sort()
    index = 0
    for i in range(len(nums)):
        if nums[i] != another[-1] and 2 * nums[i] > another[-1]:
            return -1
        if nums[i] == another[-1]:
            index = i
    return index


