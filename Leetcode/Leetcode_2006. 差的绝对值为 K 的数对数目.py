"""
2006. 差的绝对值为 K 的数对数目
给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。
|x| 的值定义为：
如果 x >= 0 ，那么值为 x 。
如果 x < 0 ，那么值为 -x 。
"""
import collections
from typing import *


def countKDifference(nums: List[int], k: int) -> int:
    nums.sort()
    dictionary = collections.OrderedDict()
    for num in nums:
        dictionary[num] = dictionary.setdefault(num, 0) + 1
    result = 0
    for num in dictionary:
        if num + k in dictionary:
            result += dictionary[num] * dictionary[num + k]
    return result


