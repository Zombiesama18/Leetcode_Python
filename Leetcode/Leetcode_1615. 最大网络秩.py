"""
1615. 最大网络秩

n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。

两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。

整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。

给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。
"""
import collections
from typing import List


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    degree_dict = collections.defaultdict(int)
    dictionary = collections.defaultdict(set)
    result = 0
    for a, b in roads:
        dictionary[a].add(b)
        dictionary[b].add(a)
        degree_dict[a] += 1
        degree_dict[b] += 1
    max_degrees = list(sorted(set(degree_dict.values()), reverse=True))[:2]
    first_class_degree, second_class_degree = [], []
    for n, d in degree_dict.items():
        if len(max_degrees) > 1 and d == max_degrees[1]:
            second_class_degree.append(n)
        elif d == max_degrees[0]:
            second_class_degree.append(n)
            first_class_degree.append(n)
    for a in first_class_degree:
        for b in second_class_degree:
            if a == b:
                continue
            if b in dictionary[a]:
                result = max(result, degree_dict[a] + degree_dict[b] - 1)
            else:
                result = max(result, degree_dict[a] + degree_dict[b])
    return result


maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]])
maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
