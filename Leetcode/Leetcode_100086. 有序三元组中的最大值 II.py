"""
100086. 有序三元组中的最大值 II

给你一个下标从 0 开始的整数数组 nums 。
请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。
下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。
"""
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        suffix = [nums[-1]]
        for i in range(len(nums) - 1, -1, -1):
            suffix.insert(0, max(nums[i], suffix[0]))
        prefix_max = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] < prefix_max:
                result = max((prefix_max - nums[i]) * suffix[i + 1], result)
            prefix_max = max(prefix_max, nums[i])
        return result


