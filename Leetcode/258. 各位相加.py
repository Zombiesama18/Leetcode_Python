"""
258. 各位相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
"""


def addDigits(num: int) -> int:
    num = list(str(num))
    while len(num) != 1:
        nextNumber = 0
        for number in num:
            nextNumber += int(number)
        num = list(str(nextNumber))
    return int(num[0])


addDigits(38)

