"""
1483. 树节点的第 K 个祖先

给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。
树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
实现 TreeAncestor 类：
TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。
"""
import collections
import math
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = math.ceil(math.log(5e4, 2))
        self.ancestors = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.log):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.log):
            if (k >> j) & 1:
                node = self.ancestors[node][j]
                if node == -1:
                    return -1
        return node
