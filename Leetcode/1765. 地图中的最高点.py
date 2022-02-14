"""
1765. 地图中的最高点
给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。
如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
你需要按照如下规则给每个单元格安排高度：
每个格子的高度都必须是非负的。
如果一个格子是是 水域 ，那么它的高度必须为 0 。
任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。
请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。
"""
import collections
from typing import *


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    """
    题目要求让矩阵中的最高高度最大，我们可以通过最大化每个格子的高度来做到这一点。由于任意相邻的格子高度差至多为 11，
    这意味着对于每个格子，其高度至多比其相邻格子中的最小高度多 11。
    题目要求水域的高度必须为 00，因此水域的高度是已经确定的值，我们可以从水域出发，推导出其余格子的高度：
    首先，计算与水域相邻的格子的高度。对于这些格子来说，其相邻格子中的最小高度即为水域的高度 00，因此这些格子的高度为 11。
    然后，计算与高度为 11 的格子相邻的、尚未被计算过的格子的高度。对于这些格子来说，其相邻格子中的最小高度为 11，因此这些格子的高度为 22。
    以此类推，计算出所有格子的高度。
    上述过程中，对于每一轮，我们考虑的是与上一轮格子相邻的、未被计算过的格子 xx，其高度必然比上一轮的格子高度多 11。
    反证之：如果格子 xx 的高度小于或等于上一轮的格子高度，那么 xx 必然会在更早的轮数被计算出来，矛盾。
    因此 xx 的高度必然比上一轮的格子高度高，同时由于题目要求任意相邻的格子高度差至多为 11，因此 xx 的高度必然比上一轮格子的高度多 11。
    可以发现，上述过程就是从水域出发，执行广度优先搜索的过程。因此，记录下所有水域的位置，然后执行广度优先搜索，
    计算出所有陆地格子的高度，即为答案。
    :param isWater:
    :return:
    """
    row, col = len(isWater), len(isWater[0])
    result = [[value - 1 for value in line] for line in isWater]
    q = collections.deque((i, j) for i, row in enumerate(isWater) for j, value in enumerate(row) if value)
    while q:
        currentX, currentY = q.popleft()
        for nextX, nextY in ((currentX - 1, currentY), (currentX + 1, currentY), (currentX, currentY - 1), (currentX, currentY + 1)):
            if 0 <= nextX < row and 0 <= nextY < col and result[nextX][nextY] == -1:
                result[nextX][nextY] = result[currentX][currentY] + 1
                q.append((nextX, nextY))
    return result


highestPeak([[0,1],[0,0]])
highestPeak([[0,0,1],[1,0,0],[0,0,0]])
