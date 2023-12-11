"""
688. 骑士在棋盘上的概率
在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。
行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
骑士继续移动，直到它走了 k 步或离开了棋盘。
返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。
"""


def knightProbability(n: int, k: int, row: int, column: int) -> float:
    dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
    for step in range(k + 1):
        for i in range(n):
            for j in range(n):
                if step == 0:
                    dp[step][i][j] = 1
                else:
                    for differenceX, differenceY in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]:
                        nextX, nextY = i + differenceX, j + differenceY
                        if 0 <= nextX < n and 0 <= nextY < n:
                            dp[step][i][j] += dp[step - 1][nextX][nextY] / 8
    return dp[k][row][column]
