"""
324. 摆动排序 II
给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
你可以假设所有输入数组都可以得到满足题目要求的结果。
"""
from typing import List


def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    sorted_nums = sorted(nums)
    right = len(nums) - 1
    left = right // 2
    index = 0
    small = True
    while index < len(nums):
        if small:
            nums[index] = sorted_nums[left]
            left -= 1
        else:
            nums[index] = sorted_nums[right]
            right -= 1
        small = not small
        index += 1
    return



