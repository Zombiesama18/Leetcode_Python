"""
5989. 元素计数
给你一个整数数组 nums ，统计并返回在 nums 中同时具有一个严格较小元素和一个严格较大元素的元素数目。
"""
import collections
from typing import List


def countElements(nums: List[int]) -> int:
    dictionary = collections.Counter(nums)
    numsSet = list(sorted(set(nums)))
    result = 0
    for i in range(1, len(numsSet) - 1):
        result += dictionary[numsSet[i]]
    return result
