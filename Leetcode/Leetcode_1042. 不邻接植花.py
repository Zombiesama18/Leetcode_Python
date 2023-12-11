"""
1042. 不邻接植花

有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。
在每个花园中，你打算种下四种花之一。
另外，所有花园 最多 有 3 条路径可以进入或离开.
你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。
花的种类用  1、2、3、4 表示。保证存在答案。
"""
import collections
import heapq
from typing import List


def gardenNoAdj(n: int, paths: List[List[int]]) -> List[int]:
    result = [0] * n
    path_dict = collections.defaultdict(list)
    for start, end in paths:
        path_dict[start].append(end)
        path_dict[end].append(start)
    for i in range(n):
        colors = [False] * 5
        for node in path_dict[i + 1]:
            colors[result[node - 1]] = True
        for j in range(1, 5):
            if not colors[j]:
                result[i] = j
                break
    return result



