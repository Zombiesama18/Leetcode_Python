"""
357. 统计各位数字都不同的数字个数
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
"""
import math


def countNumbersWithUniqueDigits(n: int) -> int:
    result = [1]
    new = 1
    temp = 0
    multiplier = 8
    while n > 0:
        if temp == 0 or temp == 1:
            new *= 9
        else:
            new *= multiplier
            multiplier -= 1
        result.append(result[-1] + new)
        n -= 1
        temp += 1
    return result[-1]


countNumbersWithUniqueDigits(4)

