"""
1590. 使数组和能被 P 整除

给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
子数组 定义为原数组中连续的一组元素。
"""
import itertools
from typing import List


def minSubarray(nums: List[int], p: int) -> int:
    s = list(itertools.accumulate(nums, initial=0))
    x = s[-1] % p
    if x == 0:
        return 0
    result = len(nums)
    last = {}
    for i, v in enumerate(s):
        last[v % p] = i
        j = last.get((v - x) % p, -len(nums))
        result = min(result, i - j)
    return result if result < len(nums) else -1


minSubarray(nums = [6,3,5,2], p = 9)
