"""
100076. 无限数组的最短子数组

给你一个下标从 0 开始的数组 nums 和一个整数 target 。
下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。
请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。
"""
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        times = target // sum(nums)
        result = times * len(nums)
        target -= times * sum(nums)
        nums = nums + nums[:-1]
        left, right = 0, 0
        temp_sum = 0
        temp_length = float('INF')
        while right < len(nums):
            temp_sum += nums[right]
            while temp_sum > target:
                temp_sum -= nums[left]
                left += 1
            if temp_sum == target:
                temp_length = min(temp_length, right - left + 1)
            right += 1
        if temp_length == float('INF'):
            return -1
        return result + temp_length



