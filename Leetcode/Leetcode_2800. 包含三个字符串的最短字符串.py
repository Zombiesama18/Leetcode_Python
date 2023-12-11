"""
2800. 包含三个字符串的最短字符串

给你三个字符串 a ，b 和 c ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。
如果有多个这样的字符串，请你返回 字典序最小 的一个。
请你返回满足题目要求的字符串。
注意：
两个长度相同的字符串 a 和 b ，如果在第一个不相同的字符处，a 的字母在字母表中比 b 的字母 靠前 ，那么字符串 a 比字符串 b 字典序小 。
子字符串 是一个字符串中一段连续的字符序列。
"""
import itertools


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        result = ""
        for a, b, c in itertools.permutations((a, b, c)):
            temp = ""
            if a in b:
                temp += b
            elif b in a:
                temp += a
            else:
                for i in range(len(a)):
                    if b.startswith(a[i:]):
                        temp += a + b[len(a[i:]):]
                        break
                    if i == len(a) - 1:
                        temp += a + b
            if temp in c:
                temp = c
            elif c not in temp:
                for i in range(len(temp)):
                    if c.startswith(temp[i:]):
                        temp += c[len(temp[i:]):]
                        break
                    if i == len(temp) - 1:
                        temp += c
            if len(temp) == len(result):
                result = min(result, temp)
            if not result or len(temp) < len(result):
                result = temp
        return result


Solution().minimumString(a = "abc", b = "bca", c = "aaa")
Solution().minimumString(a = "cac", b = "b", c = "a")
