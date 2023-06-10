"""
1330. 翻转子数组得到最大的数组值

给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
请你找到可行的最大 数组值 。
"""
from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        original_value = 0
        for i in range(len(nums) - 1):
            original_value += abs(nums[i] - nums[i + 1])
        result = original_value
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if i == 0:
                    if j == len(nums) - 1:
                        continue
                    result = max(result, original_value - abs(nums[j] - nums[j + 1]) + abs(nums[i] - nums[j + 1]))
                elif j == len(nums) - 1:
                    result = max(result, original_value - abs(nums[i - 1] - nums[i]) + abs(nums[i - 1] - nums[j]))
                else:
                    result = max(result, original_value - abs(nums[i - 1] - nums[i]) - abs(nums[j] - nums[j + 1]) +
                                 abs(nums[i - 1] - nums[j]) + abs(nums[i] - nums[j + 1]))
        return result


print(Solution().maxValueAfterReverse(nums = [2,3,1,5,4]))

