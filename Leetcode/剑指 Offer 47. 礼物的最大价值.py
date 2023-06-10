"""
剑指 Offer 47. 礼物的最大价值

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
"""
from typing import List


def maxValue(grid: List[List[int]]) -> int:
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(1, len(grid[0])):
        dp[0][i] += dp[0][i - 1] + grid[0][i]
    for i in range(1, len(grid)):
        dp[i][0] += dp[i - 1][0] + grid[i][0]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    return dp[-1][-1]


maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
