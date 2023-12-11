"""
1091. 二进制矩阵中的最短路径

给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，
该路径同时满足下述要求：
路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。
"""
import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 超时
        if grid[0][0] != 0:
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        q = collections.deque([((0, 0), {(0, 0)}, 1)])
        n = len(grid)
        while q:
            current_pos, history, result = q.popleft()
            if current_pos == (n - 1, n - 1):
                return result
            for offset_x, offset_y in directions:
                next_pos = (current_pos[0] + offset_x, current_pos[1] + offset_y)
                if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n \
                        and grid[next_pos[0]][next_pos[1]] == 0 and next_pos not in history:
                    history.add(next_pos)
                    q.append((next_pos, history.copy(), result + 1))
                    history.remove(next_pos)
        return -1

    def shortestPathBinaryMatrixFaster(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1
        q = collections.deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if x == y == n - 1:
                return dist[x][y]
            for offset_x in range(-1, 2):
                for offset_y in range(-1, 2):
                    next_x, next_y = x + offset_x, y + offset_y
                    if 0 <= next_x < n and 0 <= next_y < n:
                        if grid[next_x][next_y] == 0 and dist[next_x][next_y] > dist[x][y] + 1:
                            dist[next_x][next_y] = dist[x][y] + 1
                            q.append((next_x, next_y))
        return -1

