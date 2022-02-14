# 1976. 到达目的地的方案数（需要复习）
# 你在一个城市里，城市由 n   个路口组成，路口编号为   0   到   n - 1   ，某些路口之间有 双向   道路。
# 输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。
# 给你一个整数   n   和二维整数数组   roads   ，其中   roads[i] = [ui, vi, timei]   表示在路口   ui   和   vi   之间有一条需要花费
# timei   时间才能通过的道路。你想知道花费 最少时间   从路口   0   出发到达路口   n - 1   的方案数。
# 请返回花费 最少时间   到达目的地的 路径数目   。由于答案可能很大，将结果对   109 + 7   取余   后返回。
import collections
from collections import deque
from functools import cache


def countPaths(n: int, roads: [[int]]) -> int:
    BASE = 1000000007
    minDistance = float('INF')
    pathDict = collections.defaultdict(list)
    for road in roads:
        pathDict[road[0]].append([road[1], road[2]])
        pathDict[road[1]].append([road[0], road[2]])
    roadQueue = deque([(0, 0, 1)])
    counter = 0
    while roadQueue:
        currentNode, traversedPath, traversedNode = roadQueue.popleft()
        if currentNode == n - 1:
            if traversedPath == minDistance:
                counter = (counter + 1) % BASE
            if traversedPath < minDistance:
                minDistance = traversedPath
                counter = 1
        else:
            if traversedPath < minDistance:
                for nextNode, nextPath in pathDict[currentNode]:
                    if traversedNode & (1 << nextNode) == 0:
                        roadQueue.append((nextNode, traversedPath + nextPath, traversedNode | (1 << nextNode)))
    return counter


countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])
countPaths(2, [[1,0,10]])


def countPathsFaster(n: int, roads: [[int]]) -> int:
    BASE = 1000000007
    distance = [[float('INF')] * n for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
    for source, to, dist in roads:
        distance[source][to] = distance[to][source] = dist

    seen = set()
    for _ in range(n - 1):
        u = None
        for i in range(n):
            if i not in seen and (not u or distance[0][i] < distance[0][u]):
                u = i
        seen.add(u)
        for i in range(n):
            distance[0][i] = min(distance[0][i], distance[0][u] + distance[u][i])

    graph = collections.defaultdict(list)
    for source, to, dist in roads:
        if distance[0][to] - distance[0][source] == dist:
            graph[source].append(to)
        elif distance[0][source] - distance[0][to] == dist:
            graph[to].append(source)

    @cache
    def dfs(u: int) -> int:
        if u == n - 1:
            return 1
        result = 0
        for value in graph[u]:
            result += dfs(value)
        return result % BASE

    answer = dfs(0)
    dfs.cache_clear()
    return answer

