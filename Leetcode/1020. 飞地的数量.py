"""
1020. 飞地的数量
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
"""
from typing import *


def numEnclaves(grid: List[List[int]]) -> int:
    visited = set()
    row, col = len(grid), len(grid[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(currentX, currentY):
        if (currentX, currentY) in visited or grid[currentX][currentY] != 1:
            return
        visited.add((currentX, currentY))
        for direction in directions:
            nextX, nextY = currentX + direction[0], currentY + direction[1]
            if 0 <= nextX < row and 0 <= nextY < col and (nextX, nextY) not in visited and grid[nextX][nextY] == 1:
                bfs(nextX, nextY)
        return

    for j in range(col):
        bfs(0, j)
        bfs(row - 1, j)
    for i in range(row):
        bfs(i, 0)
        bfs(i, col - 1)
    result = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                result += 1
    return result - len(visited)


numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])

