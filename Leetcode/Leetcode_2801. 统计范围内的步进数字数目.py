"""
2801. 统计范围内的步进数字数目

给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
由于答案可能很大，请你将它对 109 + 7 取余 后返回。
注意：步进数字不能有前导 0 。
"""
from functools import cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        self.MOD = 10 ** 9 + 7
        return (self.search(high, 0, 0, True, False) - self.search(str(int(low) - 1), 0, 0, True, False)) % self.MOD

    @cache
    def search(self, s, i, pre, is_limit, is_num):
        if i == len(s):
            return int(is_num)
        result = 0
        if not is_num:
            result = self.search(s, i + 1, pre, False, False)
        if is_num:
            low = 0
        else:
            low = 1
        if is_limit:
            up = int(s[i])
        else:
            up = 9
        for d in range(low, up + 1):
            if not is_num or abs(d - pre) == 1:
                result += self.search(s, i + 1, d, is_limit and d == up, True)
        return result % self.MOD


Solution().countSteppingNumbers(low = "90", high = "101")

