"""
2787. 将一个数字表示成幂的和的方案数

给你两个 正 整数 n 和 x 。
请你返回将 n 表示成一些 互不相同 正整数的 x 次幂之和的方案数。换句话说，
你需要返回互不相同整数 [n1, n2, ..., nk] 的集合数目，满足 n = n1x + n2x + ... + nkx 。
由于答案可能非常大，请你将它对 109 + 7 取余后返回。
比方说，n = 160 且 x = 3 ，一个表示 n 的方法是 n = 23 + 33 + 53 。
"""
import math
from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        max_num = math.floor(math.pow(n + 1, 1 / x))
        dp = [[0] * (n + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1
        for i in range(1, max_num + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= i ** x:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - i ** x]) % MOD
        return dp[max_num][n]
