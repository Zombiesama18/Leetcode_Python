"""
686. 重复叠加字符串匹配
给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
"""
import collections
import math
import random


class Solution:
    def robinKarp(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        k1 = 10 ** 9 + 7
        k2 = 1337
        mod1 = random.randrange(k1) + k1
        mod2 = random.randrange(k2) + k2
        hash_needle = 0
        for char in needle:
            hash_needle = (hash_needle * mod2 + ord(char)) % mod1
        hash_haystack = 0
        for i in range(m - 1):
            hash_haystack = (hash_haystack * mod2 + ord(haystack[i % n])) % mod1
        extra = pow(mod2, m - 1, mod1)
        for i in range(m - 1, n + m - 1):
            hash_haystack = (hash_haystack * mod2 + ord(haystack[i % n])) % mod1
            if hash_haystack == hash_needle:
                return i - m + 1
            hash_haystack = (hash_haystack - extra * ord(haystack[(i - m + 1) % n])) % mod1
            hash_haystack = (hash_haystack + mod1) % mod1
        return -1

    def repeatedStringMatchRabinKarp(self, a: str, b: str) -> int:
        """
        命题【存在重复叠加字符串 s_1 = a \\dots a, 使得字符串 b 成为叠加后的字符串 s_1 的子串】等价于【字符串 b 成为无线重复叠加
        字符串 s_2 = aa \\dots 的子串】。而后者成立的前提是任一 s_2[i:\\infty],0 \\leq i < len(a) 以 b 为前缀，即 b 可以从第一个
        叠加的 a 开始匹配成功
        因此可以分为两种情况：
        \\begin{itemize}
        \\item b 可以是从第一个叠加的 a 开始匹配成功，则明显匹配的下标越小，最终需要的叠加数目 k 越小，记成功匹配的最小下标为 index,
        0 \\leq index < len(a), 于是：
        k = \\left\\{
        \\begin{aligned}
        1 & , & len(b) \\leq len(a) - index \\
        \\lceil \\frac{len(b) - \\lceil len(a) - index \\rceil}{len(a)} \\rceil + 1 & , & len(b) > len(a) - index
        \\end{aligned}
        \\right
        \\item b 无法从第一个叠加的 a 开始匹配成功，说明不存在重复叠加字符串 s_1 = a \\dots a,
        使得字符串 b 成为叠加后的字符串 s_1 = a \\ dots a 的子串。 \\
        在应用 Robin-Karp 算法时，被匹配字符串是循环叠加的字符串，所以下标要进行取余操作，并且匹配终止的条件为 b 开始匹配的位置超过第一个
        叠加的 a 。我们采用随机数来生成 Robin-Karp 算法哈希函数，希望避免后序哈希冲突的发生。
        """
        n, m = len(a), len(b)
        index = self.robinKarp(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2

    def KMP(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pi[i] = j
        i, j = 0, 0
        while i - j < n:
            while j > 0 and haystack[i % n] != needle[j]:
                j = pi[j - 1]
            if haystack[i % n] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

    def repeatedStringMatchKMP(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.KMP(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2



