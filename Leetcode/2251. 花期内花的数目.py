"""
2251. 花期内花的数目
给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。
同时给你一个下标从 0 开始大小为 n 的整数数组 persons ，persons[i] 是第 i 个人来看花的时间。
请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。
"""
import collections
from typing import List


def fullBloomFlowers(flowers: List[List[int]], persons: List[int]) -> List[int]:
    difference = collections.defaultdict(int)
    for start, end in flowers:
        difference[start] += 1
        difference[end + 1] -= 1
    times = sorted(difference.keys())
    result = [0] * len(persons)
    index, summation = 0, 0
    for i, person in sorted(zip(range(len(persons)), persons), key=lambda x: x[1]):
        while index < len(times) and times[index] <= person:
            summation += difference[times[index]]
            index += 1
        result[i] = summation
    return result


fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11])

