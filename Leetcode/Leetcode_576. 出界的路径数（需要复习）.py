# 576. 出界的路径数
# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。
# 你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
# 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。
# 因为答案可能非常大，返回对 109 + 7 取余 后的结果。
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    BASE = 10**9 + 7
    dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
    dp[0][startRow][startColumn] = 1
    result = 0
    for i in range(maxMove):
        for j in range(m):
            for k in range(n):
                if dp[i][j][k] > 0:
                    for nextJ, nextK in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                        if 0 <= nextJ < m and 0 <= nextK < n:
                            dp[i + 1][nextJ][nextK] = (dp[i + 1][nextJ][nextK] + dp[i][j][k]) % BASE
                        else:
                            result = (result + dp[i][j][k]) % BASE
    return result


