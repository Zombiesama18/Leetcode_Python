"""
1016. 子串能表示从 1 到 N 数字的二进制串

给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，
其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。
子字符串 是字符串中连续的字符序列。
"""


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        history = set()
        s = list(map(int, s))
        for i, x in enumerate(s):
            if x == 0:
                continue
            j = i + 1
            while x <= n:
                history.add(x)
                if j == len(s):
                    break
                x = (x << 1) | s[j]
                j += 1
        return len(history) == n


Solution().queryString(s = "0110", n = 3)
