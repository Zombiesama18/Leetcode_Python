"""
6015. 统计可以被 K 整除的下标对数目
给你一个下标从 0 开始、长度为 n 的整数数组 nums 和一个整数 k ，返回满足下述条件的下标对 (i, j) 的数目：
0 <= i < j <= n - 1 且
nums[i] * nums[j] 能被 k 整除。
"""
import collections
import math
from typing import *


def coutPairs(nums: List[int], k: int) -> int:
    dividedByGCD = list(collections.Counter(math.gcd(num, k) for num in nums).items())
    result = 0
    for i in range(len(dividedByGCD)):
        number1, counter1 = dividedByGCD[i]
        if number1 * number1 % k == 0:
            result += counter1 * (counter1 - 1) // 2
        for j in range(i + 1, len(dividedByGCD)):
            number2, counter2 = dividedByGCD[j]
            if number1 * number2 % k == 0:
                result += counter1 * counter2
    return result

