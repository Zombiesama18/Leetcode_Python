"""
5300. 有向无环图中一个节点的所有祖先
给你一个正整数 n ，它表示一个 有向无环图 中节点的数目，节点编号为 0 到 n - 1 （包括两者）。
给你一个二维整数数组 edges ，其中 edges[i] = [fromi, toi] 表示图中一条从 fromi 到 toi 的单向边。
请你返回一个数组 answer，其中 answer[i]是第 i 个节点的所有 祖先 ，这些祖先节点 升序 排序。
如果 u 通过一系列边，能够到达 v ，那么我们称节点 u 是节点 v 的 祖先 节点。
"""
import collections
from typing import List


def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    graph = collections.defaultdict(set)
    for source, destination in edges:
        graph[destination].add(source)
    ancestorDict = collections.defaultdict(set)
    flags = [False] * n

    def search(node):
        for ancestor in graph[node]:
            ancestorDict[node].add(ancestor)
            if flags[ancestor]:
                ancestorDict[node].update(ancestorDict[ancestor])
            else:
                search(ancestor)
                ancestorDict[node].update(ancestorDict[ancestor])
        flags[node] = True
        return

    for i in range(n):
        search(i)
    return [sorted(ancestorDict[x]) for x in range(n)]


getAncestors(n=8, edges=[[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]])
getAncestors(n=10, edges=[[5, 2], [8, 7], [7, 2], [8, 3], [1, 6], [9, 0]])
