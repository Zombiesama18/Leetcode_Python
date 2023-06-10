"""
2357. 使数组中所有元素都等于零

给你一个非负整数数组 nums 。在一步操作中，你必须：

选出一个正整数 x ，x 需要小于或等于 nums 中 最小 的 非零 元素。
nums 中的每个正整数都减去 x。
返回使 nums 中所有元素都等于 0 需要的 最少 操作数。
"""
from typing import List


def minimumOperations(nums: List[int]) -> int:
    nums = set(nums)
    return len(nums) - 1 if 0 in nums else len(nums)


