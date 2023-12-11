"""
招商银行-02. 公园规划
公园规划小组为了让公园景观层次丰富，决定按以下方案对各花坛内的植物进行统一规划：
一条小路两端的花坛不能栽种同一种花
与同一花坛相连的两个花坛也不能栽种同一种花。
已知公园内有编号为 0 ~ num-1的若干花坛，任意两个花坛均可通过小路直接或间接到达。
公园中共有 num-1 条双向小路连接花坛，roads[i] = [x, y] 表示花坛 x 和花坛 y 之间存在小路将二者相连。
请返回这些花坛最少需要几种花。
"""
import collections
from typing import List


def numFlowers(roads: List[List[int]]) -> int:
    graph = collections.defaultdict(set)
    for road in roads:
        graph[road[0]].add(road[1])
    for node in graph:
        if node > 1:
            graph[node].add(node - 2)
        if node < len(roads) - 2:
            graph[node].add(node + 2)
    return max(len(value) + 1 for value in graph.values())


numFlowers(roads = [[0,1],[0,2],[1,3],[2,5],[3,6],[5,4]])

