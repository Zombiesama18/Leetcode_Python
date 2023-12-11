"""
400. 第 N 位数字
给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。
"""


def findNthDigit(n: int) -> int:
    bits, counter = 1, 9
    while n > bits * counter:
        n -= bits * counter
        bits += 1
        counter *= 10
    index = n - 1
    start = 10 ** (bits - 1)
    num = start + index // bits
    digitIndex = index % bits
    return num // 10 ** (bits - digitIndex - 1) % 10


findNthDigit(320)

