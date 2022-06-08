"""
2279. 装满石头的背包的最大数量
现有编号从 0 到 n - 1 的 n 个背包。给你两个下标从 0 开始的整数数组 capacity 和 rocks 。第 i 个背包最大可以装 capacity[i] 块石头，
当前已经装了 rocks[i] 块石头。另给你一个整数 additionalRocks ，表示你可以放置的额外石头数量，石头可以往 任意 背包中放置。
请你将额外的石头放入一些背包中，并返回放置后装满石头的背包的 最大 数量。
"""
import collections
from typing import List


def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    differenceDict = collections.defaultdict(int)
    for cap, rock in zip(capacity, rocks):
        differenceDict[cap - rock] += 1
    differences = list(differenceDict.keys())
    differences.sort()
    result = 0
    for difference in differences:
        if additionalRocks >= difference * differenceDict[difference]:
            additionalRocks -= difference * differenceDict[difference]
            result += differenceDict[difference]
        else:
            result += additionalRocks // difference
            break
        if additionalRocks == 0:
            break
    return result

