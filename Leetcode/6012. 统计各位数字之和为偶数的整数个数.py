"""
6012. 统计各位数字之和为偶数的整数个数
给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。
正整数的 各位数字之和 是其所有位上的对应数字相加的结果。
"""


def countEven(num: int) -> int:
    result = 0
    currentNumber = 2
    while currentNumber <= num:
        if sum([int(i) for i in str(currentNumber)]) % 2 == 0:
            result += 1
        currentNumber += 1
    return result
