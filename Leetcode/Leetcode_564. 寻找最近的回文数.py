"""
564. 寻找最近的回文数
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
“最近的”定义为两个整数差的绝对值最小。
"""


def nearestPalindromic(n: str) -> str:
    length = len(n)
    candidates = [10 ** (length - 1) - 1, 10 ** length + 1]
    selfPrefix = int(n[:(length + 1) // 2])
    for x in range(selfPrefix - 1, selfPrefix + 2):
        y = x if length % 2 == 0 else x // 10
        while y:
            x = x * 10 + y % 10
            y //= 10
        candidates.append(x)
    result = -1
    selfNumber = int(n)
    for candidate in candidates:
        if candidate != selfNumber:
            if result == -1 or abs(candidate - selfNumber) < abs(result - selfNumber) or \
                    abs(candidate - selfNumber) == abs(result - selfNumber) and candidate < result:
                result = candidate
    return str(result)


nearestPalindromic('123')
nearestPalindromic('1')
