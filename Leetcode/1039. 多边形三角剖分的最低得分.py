"""
1039. 多边形三角剖分的最低得分

你有一个凸的 n 边形，其每个顶点都有一个整数值。给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。
假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，
三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和。
返回 多边形进行三角剖分后可以得到的最低分 。
"""
from functools import cache
from typing import List


def minScoreTriangulation(values: List[int]) -> int:

    @cache
    def dfs(i, j):
        if j - i < 2:
            return 0
        return min(dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k] for k in range(i + 1, j))

    return dfs(0, len(values) - 1)


print(minScoreTriangulation(values = [1,3,1,4,1,5]))
