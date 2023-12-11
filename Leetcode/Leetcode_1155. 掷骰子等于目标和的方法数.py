"""
1155. 掷骰子等于目标和的方法数

这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
答案可能很大，你需要对 109 + 7 取模 。
"""
import functools


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.MOD = 10 ** 9 + 7
        return self.dfs(n, k, target)

    @functools.cache
    def dfs(self, n: int, k: int, target: int):
        if n == 1:
            return int(target <= k)
        temp = 0
        for i in range(1, k + 1):
            if target - i > 0:
                temp = (temp + self.dfs(n - 1, k, target - i)) % self.MOD
            else:
                break
        return temp
