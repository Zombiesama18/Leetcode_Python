"""
2681. 英雄的力量

给你一个下标从 0 开始的整数数组 nums ，它表示英雄的能力值。如果我们选出一部分英雄，这组英雄的 力量 定义为：
i0 ，i1 ，... ik 表示这组英雄在数组中的下标。那么这组英雄的力量为
max(nums[i0],nums[i1] ... nums[ik])2 * min(nums[i0],nums[i1] ... nums[ik]) 。
请你返回所有可能的 非空 英雄组的 力量 之和。由于答案可能非常大，请你将结果对 109 + 7 取余。
"""
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        prefix_sum = 0
        result = 0
        MOD = 10 ** 9 + 7
        for num in nums:
            result = (result + num * num * (num + prefix_sum)) % MOD
            prefix_sum = (prefix_sum * 2 + num) % MOD
        return result

