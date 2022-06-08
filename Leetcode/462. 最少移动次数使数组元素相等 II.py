"""
462. 最少移动次数使数组元素相等 II
给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。
"""
from typing import List


# 因为对于任何一个子序列，头尾元素的差值是定值。于是不断地去除头尾元素，最后只剩下中位数
def minMoves2(nums: List[int]) -> int:
    nums.sort()
    return sum([abs(num - nums[len(nums) // 2]) for num in nums])


minMoves2([1,0,0,8,6])
