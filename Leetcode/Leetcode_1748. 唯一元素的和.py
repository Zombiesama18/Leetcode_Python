"""
1748. 唯一元素的和
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
请你返回 nums 中唯一元素的 和 。
"""
import collections


def sumOfUnique(nums: [int]) -> int:
    nums = collections.Counter(nums)
    result = 0
    for num in nums:
        if nums[num] == 1:
            result += num
    return result


