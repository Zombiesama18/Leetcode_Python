"""
5953. 子数组范围和
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
返回 nums 中 所有 子数组范围的 和 。
子数组是数组中一个连续 非空 的元素序列。
"""
import heapq


def subArrayRanges(nums: [int]) -> int:
    result = 0
    for i in range(len(nums) - 1):
        max_value, min_value = nums[i], nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] > max_value:
                max_value = nums[j]
            if nums[j] < min_value:
                min_value = nums[j]
            result += max_value - min_value
    return result


subArrayRanges([1,2,3])
subArrayRanges([1,3,3])
subArrayRanges([4,-2,-3,4,1])
