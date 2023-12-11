"""
2427. 公因子的数目

给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
"""
import math


def commonFactors(a: int, b: int) -> int:
    set_a, set_b = set(), set()
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            set_a.add(i)
            set_a.add(a // i)
    for i in range(1, int(math.sqrt(b)) + 1):
        if b % i == 0:
            set_b.add(i)
            set_b.add(b // i)
    return len(set_a.intersection(set_b))


commonFactors(32, 408)
