"""
6005. 使数组变成交替数组的最少操作数
给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。
如果满足下述条件，则数组 nums 是一个 交替数组 ：
nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。
返回使数组变成交替数组的 最少操作数 。
"""
import collections
from typing import *


def minimumOperations(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    numsEven, numsOdd = [], []
    for i in range(len(nums)):
        if i % 2 == 0:
            numsEven.append(nums[i])
        else:
            numsOdd.append(nums[i])
    counterEven, counterOdd = collections.Counter(numsEven), collections.Counter(numsOdd)
    counterEven = sorted(counterEven.items(), key=lambda x: -x[1])
    counterOdd = sorted(counterOdd.items(), key=lambda x: -x[1])
    if counterEven[0][0] != counterOdd[0][0]:
        return len(nums) - counterEven[0][1] - counterOdd[0][1]
    return min(len(nums) - counterEven[0][1] - (0 if len(counterOdd) == 1 else counterOdd[1][1]),
               len(nums) - counterOdd[0][1] - (0 if len(counterEven) == 1 else counterEven[1][1]))


minimumOperations([3,1,3,2,4,3])
minimumOperations([1,2,2,2,2])
