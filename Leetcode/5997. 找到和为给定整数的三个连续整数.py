"""
5997. 找到和为给定整数的三个连续整数
给你一个整数 num ，请你返回三个连续的整数，它们的 和 为 num 。如果 num 无法被表示成三个连续整数的和，请你返回一个 空 数组。
"""
from typing import *


def sumOfThree(num: int) -> List[int]:
    if num % 3 != 0:
        return []
    return [num // 3 - 1, num // 3, num // 3 + 1]

