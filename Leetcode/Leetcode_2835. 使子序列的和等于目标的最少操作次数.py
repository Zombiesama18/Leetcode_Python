"""
2835. 使子序列的和等于目标的最少操作次数

给你一个下标从 0 开始的数组 nums ，它包含 非负 整数，且全部为 2 的幂，同时给你一个整数 target 。
一次操作中，你必须对数组做以下修改：
选择数组中一个元素 nums[i] ，满足 nums[i] > 1 。
将 nums[i] 从数组中删除。
在 nums 的 末尾 添加 两个 数，值都为 nums[i] / 2 。
你的目标是让 nums 的一个 子序列 的元素和等于 target ，请你返回达成这一目标的 最少操作次数 。如果无法得到这样的子序列，请你返回 -1 。
数组中一个 子序列 是通过删除原数组中一些元素，并且不改变剩余元素顺序得到的剩余数组。
"""
import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        num_counter = collections.Counter()
        nums_sum = 0
        for num in nums:
            nums_sum += num
            num_counter[num] += 1
        if nums_sum < target:
            return -1
        index = current_sum = result = 0
        while 1 << index <= target:
            current_sum += num_counter[1 << index] << index
            mask = (1 << (index + 1)) - 1
            index += 1
            if current_sum >= target & mask:
                continue
            result += 1
            while num_counter[1 << index] == 0:
                result += 1
                index += 1
        return result

