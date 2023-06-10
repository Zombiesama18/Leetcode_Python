"""
1000. 合并石头的最低成本

有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
"""
from typing import List


def mergeStones(stones: List[int], k: int) -> int:
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1
    dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    summation = [0]
    for i in range(1, n + 1):
        summation.append(summation[i - 1] + stones[i - 1])
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for m in range(2, k + 1):
                dp[i][j][m] = float('inf')
        dp[i][i][1] = 0
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            for m in range(2, k + 1):
                for p in range(i, j, k - 1):
                    dp[i][j][m] = min(dp[i][j][m], dp[i][p][1] + dp[p + 1][j][m - 1])
            dp[i][j][1] = dp[i][j][k] + summation[j] - summation[i - 1]
    return dp[1][n][1]



