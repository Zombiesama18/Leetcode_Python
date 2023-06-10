"""
2404. 出现最频繁的偶数元素

给你一个整数数组 nums ，返回出现最频繁的偶数元素。
如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。
"""
import collections
from typing import List


def mostFrequentEven(nums: List[int]) -> int:
    counts = collections.Counter(nums)
    counts = list(sorted(counts.items(), key=lambda x: (-x[1], x[0])))
    for num, freq in counts:
        if num % 2 == 0:
            return num
    return -1

