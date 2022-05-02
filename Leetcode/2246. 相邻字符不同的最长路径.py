"""
2246. 相邻字符不同的最长路径
给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、
长度为 n 的数组 parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。
另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。
请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。
"""
import collections
from typing import List


def longestPath(parent: List[int], s: str) -> int:
    graph = collections.defaultdict(list)
    for i, p in enumerate(parent):
        graph[p].append(i)
    result = 0

    def dfs(x):
        nonlocal result
        maxLen = 0
        for child in graph[x]:
            length = dfs(child) + 1
            if s[child] != s[x]:
                result = max(result, maxLen + length)
                maxLen = max(maxLen, length)
        return maxLen

    dfs(0)
    return result + 1


longestPath(parent = [-1,0,0,1,1,2], s = "abacbe")

