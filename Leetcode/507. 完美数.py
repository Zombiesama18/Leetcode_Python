"""
507. 完美数
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
"""
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        result, index, target = 1, 2, math.sqrt(num)
        while index <= target:
            if num % index == 0:
                result += index
                result += num // index
                if result > num:
                    return False
            index += 1
        return result == num


s = Solution()
s.checkPerfectNumber(28)
s.checkPerfectNumber(1)

