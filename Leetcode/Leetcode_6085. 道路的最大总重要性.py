"""
6085. 道路的最大总重要性
给你一个整数 n ，表示一个国家里的城市数目。城市编号为 0 到 n - 1 。
给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] 表示城市 ai 和 bi 之间有一条 双向 道路。
你需要给每个城市安排一个从 1 到 n 之间的整数值，且每个值只能被使用 一次 。道路的 重要性 定义为这条道路连接的两座城市数值 之和 。
请你返回在最优安排下，所有道路重要性 之和 最大 为多少。
"""
import collections
from typing import List


def maximumImportance(n: int, roads: List[List[int]]) -> int:
    degrees = [0] * n
    distribution = [0] * n
    for start, to in roads:
        degrees[start] += 1
        degrees[to] += 1
    degrees = [(i, d) for i, d in enumerate(degrees)]
    degrees.sort(key=lambda x: x[1], reverse=True)
    points = n
    for index, _ in degrees:
        distribution[index] = points
        points -= 1
    result = 0
    for start, to in roads:
        result += distribution[start] + distribution[to]
    return result


