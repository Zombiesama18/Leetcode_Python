"""
1015. 可被 K 整除的最小整数

给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
返回 n 的长度。如果不存在这样的 n ，就返回-1。
注意： n 不符合 64 位带符号整数。
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        residual, length = 1 % k, 1
        his = {residual}
        while residual != 0:
            residual = (residual * 10 + 1) % k
            length += 1
            if residual in his:
                return -1
            his.add(residual)
        return length
