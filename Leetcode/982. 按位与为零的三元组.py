"""
982. 按位与为零的三元组

给你一个整数数组 nums ，返回其中 按位与三元组 的数目。
按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：
0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
"""
import collections
import itertools
from typing import List


def countTriplets(self, nums: List[int]) -> int:
    counter = collections.Counter((x & y) for x in nums for y in nums)
    result = 0

    counter2 = collections.Counter(nums)
    for num1, num2 in itertools.product(counter.keys(), counter2.keys()):
        if num1 & num2 == 0:
            result += counter[num1] * counter2[num2]
    return result
