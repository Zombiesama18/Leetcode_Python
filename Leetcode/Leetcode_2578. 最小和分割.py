"""
2578. 最小和分割

给你一个正整数 num ，请你将它分割成两个非负整数 num1 和 num2 ，满足：
num1 和 num2 直接连起来，得到 num 各数位的一个排列。
换句话说，num1 和 num2 中所有数字出现的次数之和等于 num 中所有数字出现的次数。
num1 和 num2 可以包含前导 0 。
请你返回 num1 和 num2 可以得到的和的 最小 值。
注意：
num 保证没有前导 0 。
num1 和 num2 中数位顺序可以与 num 中数位顺序不同。
"""


class Solution:
    def splitNum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        num1 = num2 = 0
        while len(num) >= 1:
            num1 = num1 * 10 + int(num.pop(0))
            num2 = num2 * 10 + int(num.pop(0))
        if len(num) == 1:
            result = min(num1 * 10 + int(num[0]) + num2, num1 + num2 * 10 + int(num[0]))
        else:
            result = num1 + num2
        return result



Solution().splitNum(4325)

