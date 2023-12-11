"""
693. 交替位二进制数
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
"""


def hasAlternatingBits(n: int) -> bool:
    lastNumber = 2
    while n:
        if n & 1 == lastNumber:
            return False
        lastNumber = n & 1
        n >>= 1
    return True


hasAlternatingBits(n = 5)
