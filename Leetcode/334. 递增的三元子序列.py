"""
334. 递增的三元子序列
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
"""
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    minValue, secondMinValue = nums[0], float('inf')
    for i in range(1, len(nums)):
        if nums[i] > secondMinValue:
            return True
        if nums[i] > minValue:
            secondMinValue = nums[i]
        else:
            minValue = nums[i]
    return False


increasingTriplet([1,2,3,4,5])
increasingTriplet([2,1,5,0,4,6])
increasingTriplet([5,4,3,2,1])
increasingTriplet([20,100,10,12,101,5,13])
