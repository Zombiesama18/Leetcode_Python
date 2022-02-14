"""
397. 整数替换
给定一个正整数 n ，你可以做如下操作：
如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
n 变为 1 所需的最小替换次数是多少？
"""


def integerReplacement(n: int) -> int:
    def helper(number):
        if number == 1:
            return 0
        if number % 2 == 0:
            return 1 + helper(number // 2)
        if number % 4 == 1:
            return 2 + helper(number // 2)
        if number == 3:
            return 2
        return 2 + helper(number // 2 + 1)

    return helper(n)


integerReplacement(8)
integerReplacement(7)
