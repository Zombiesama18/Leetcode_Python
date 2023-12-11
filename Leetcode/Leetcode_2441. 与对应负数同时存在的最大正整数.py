"""
2441. 与对应负数同时存在的最大正整数

给你一个 不包含 任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。
返回正整数 k ，如果不存在这样的整数，返回 -1 。
"""
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = -1
        for num in nums:
            if num > 0 and -num in num_set:
                result = max(result, num)
        return result
