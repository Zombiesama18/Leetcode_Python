"""
980. 不同路径 III

在二维网格 grid 上，有 4 种类型的方格：
1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。
"""
import functools
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        history = 0
        self.num_row, self.num_col = len(grid), len(grid[0])
        self.target = (1 << self.num_row * self.num_col) - 1
        for i in range(self.num_row):
            for j in range(self.num_col):
                if grid[i][j] == -1:
                    history |= 1 << (i * self.num_col + j)
                if grid[i][j] == 1:
                    start_x, start_y = i, j
        return self.dfs(start_x, start_y, history)

    @functools.cache
    def dfs(self, x, y, history):
        if x < 0 or x >= self.num_row or y < 0 or y >= self.num_col or history >> (x * self.num_col + y) & 1:
            return 0
        history |= 1 << (x * self.num_col + y)
        if self.grid[x][y] == 2:
            return history == self.target
        return (self.dfs(x + 1, y, history) + self.dfs(x - 1, y, history)
                + self.dfs(x, y + 1, history) + self.dfs(x, y - 1, history))

