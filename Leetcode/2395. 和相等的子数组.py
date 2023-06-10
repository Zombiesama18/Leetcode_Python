"""
2395. 和相等的子数组

给你一个下标从 0  开始的整数数组  nums  ，判断是否存在  两个  长度为  2  的子数组且它们的  和  相等。注意，
这两个子数组起始位置的下标必须  不相同  。
如果这样的子数组存在，请返回  true，否则返回  false  。
子数组 是一个数组中一段连续非空的元素组成的序列。
"""
from typing import List


def findSubarrays(nums: List[int]) -> bool:
    history = set()
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum in history:
            return True
        history.add(current_sum)
    return False


findSubarrays([77,95,90,98,8,100,88,96,6,40,86,56,98,96,40,52,30,33,97,72,54,15,33,77,78,8,21,47,99,48])

