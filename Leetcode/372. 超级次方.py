"""
372. 超级次方
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
"""


def superPow(a: int, b: [int]) -> int:
    return pow(a, int(''.join(map(str, b))), 1337)


