"""
2870. 使数组为空的最少操作次数

给你一个下标从 0 开始的正整数数组 nums 。
你可以对数组执行以下两种操作 任意次 ：
从数组中选择 两个 值 相等 的元素，并将它们从数组中 删除 。
从数组中选择 三个 值 相等 的元素，并将它们从数组中 删除 。
请你返回使数组为空的 最少 操作次数，如果无法达成，请返回 -1 。
"""
import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = collections.Counter(nums)
        result = 0
        for value in nums.values():
            num_of_3 = 0
            temp_sum = float('INF')
            while num_of_3 * 3 <= value:
                if (value - num_of_3 * 3) % 2 == 0:
                    temp_sum = min(num_of_3 + (value - num_of_3 * 3) // 2, temp_sum)
                num_of_3 += 1
            if temp_sum == float('INF'):
                return -1
            result += temp_sum
        return result
