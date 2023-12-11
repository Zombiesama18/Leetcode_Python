"""
2876. 有向图访问计数

现有一个有向图，其中包含 n 个节点，节点编号从 0 到 n - 1 。此外，该图还包含了 n 条有向边。
给你一个下标从 0 开始的数组 edges ，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的边。
想象在图上发生以下过程：
你从节点 x 开始，通过边访问其他节点，直到你在 此过程 中再次访问到之前已经访问过的节点。
返回数组 answer 作为答案，其中 answer[i] 表示如果从节点 i 开始执行该过程，你可以访问到的不同节点数。
"""
import collections
from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        self.edge_connection = [collections.defaultdict(int) for _ in range(len(edges))]
        self.edges = edges

    def dfs(self, current_node, counter):
        if self.edges[current_node] in self.edge_connection:
            self.edge_connection[current_node] = counter + self.edge_connection[self.edges[current_node]]
            return
        else:



