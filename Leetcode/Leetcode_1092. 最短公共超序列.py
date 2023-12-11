"""
1092. 最短公共超序列

给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，
那么 S 就是 T 的子序列）
"""
from functools import cache


class shortestCommonSupersequence:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def recursion_solution(self, s, t):
        if not s:
            return t
        if not t:
            return s
        if s[-1] == t[-1]:
            return self.recursion_solution(s[:-1], t[:-1]) + s[-1]
        result1 = self.recursion_solution(s[:-1], t)
        result2 = self.recursion_solution(s, t[-1])
        if len(result1) < len(result2):
            return result1 + s[-1]
        return result2 + t[-1]

    def memorized_search_primary(self, s, t):
        return self.primary_dfs(len(s) - 1, len(t) - 1)

    def memorized_search_secondary(self, s, t):

    @cache
    def primary_dfs(self, s, t, i: int, j:int):
        if i < 0:
            return t[:j + 1]
        if j < 0:
            return s[:i + 1]
        if s[i] == t[j]:
            return self.primary_dfs(s, t, i - 1, j - 1) + s[i]
        result1 = self.primary_dfs(i - 1, j)
        result2 = self.primary_dfs(i, j - 1)
        if len(result1) < len(result2):
            return result1 + s[i]
        return result2 + t[j]

    def secondary_dfs(self, s, t, i: int, j:int):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if s[i] == t[j]:
            return self.secondary_dfs(s, t, i - 1, j - 1) + 1
        return min(self.secondary_dfs(s, t, i - 1, j), self.secondary_dfs(s, t, i, j - 1)) + 1

    def generate_result(self, s, t, i, j):
        if i < 0:
            return t[:j + 1]
        if j < 0:
            return s[:i + 1]
        if s[i] == t[j]:
            return self.generate_result(s, t, i - 1, j - 1) + s[i]
        if self.secondary_dfs(s, t, i, j) == self.secondary_dfs(s, t, i - 1, j) + 1:
            return self.generate_result(s, t, i - 1, j) + s[i]
        return self.generate_result(s, t, i, j - 1) + t[j]


