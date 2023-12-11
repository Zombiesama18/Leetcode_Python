"""
5963. 反转两次的数字
反转 一个整数意味着倒置它的所有位。
例如，反转 2021 得到 1202 。反转 12300 得到 321 ，不保留前导零 。
给你一个整数 num ，反转 num 得到 reversed1 ，接着反转 reversed1 得到 reversed2 。
如果 reversed2 等于 num ，返回 true ；否则，返回 false 。
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0

