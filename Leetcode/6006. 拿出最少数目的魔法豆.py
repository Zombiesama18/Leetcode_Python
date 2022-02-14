"""
6006. 拿出最少数目的魔法豆
给你一个 正 整数数组 beans ，其中每个整数表示一个袋子里装的魔法豆的数目。
请你从每个袋子中 拿出 一些豆子（也可以 不拿出），使得剩下的 非空 袋子中（即 至少 还有 一颗 魔法豆的袋子）魔法豆的数目 相等 。
一旦魔法豆从袋子中取出，你不能将它放到任何其他的袋子中。
请你返回你需要拿出魔法豆的 最少数目。
"""
import collections
from typing import *


def minimumRemoval(beans: List[int]) -> int:
    result = float('INF')
    summation = sum(beans)
    dictionary = collections.Counter(beans)
    dictionary = sorted(dictionary.items(), key=lambda x: x[0])
    tempPosition = 0
    for number, counter in dictionary:
        result = min(summation - number * (len(beans) - tempPosition), result)
        tempPosition += counter
    return result


minimumRemoval([4,1,6,5])
minimumRemoval([2,10,3,2])
