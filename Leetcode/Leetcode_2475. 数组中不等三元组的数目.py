"""
2475. 数组中不等三元组的数目

给你一个下标从 0 开始的正整数数组 nums 。请你找出并统计满足下述条件的三元组 (i, j, k) 的数目：
0 <= i < j < k < nums.length
nums[i]、nums[j] 和 nums[k] 两两不同 。
换句话说：nums[i] != nums[j]、nums[i] != nums[k] 且 nums[j] != nums[k] 。
返回满足上述条件三元组的数目。
"""
import collections
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        nums = list(counter.keys())
        result = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    result += counter[nums[i]] * counter[nums[j]] * counter[nums[k]]
        return result



