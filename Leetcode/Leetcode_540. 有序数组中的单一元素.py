"""
540. 有序数组中的单一元素
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
"""
from typing import *


def singleNonDuplicate(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    lastNumber, counter = nums[0], 1
    for i in range(1, len(nums)):
        if nums[i] != lastNumber and counter == 1:
            return lastNumber
        if nums[i] != lastNumber:
            lastNumber = nums[i]
            counter = 1
        else:
            counter += 1
    return lastNumber


def singleNonDuplicateVersion2(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 0:
            if nums[mid] == nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        else:
            if nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid
    return nums[left]


singleNonDuplicateVersion2([1,1,2,3,3,4,4,8,8])
singleNonDuplicateVersion2([3,3,7,7,10,11,11])


