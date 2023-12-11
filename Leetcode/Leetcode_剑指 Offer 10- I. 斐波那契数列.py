# 剑指 Offer 10- I. 斐波那契数列
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
import heapq


def fib(n: int) -> int:
    BASE = 1000000007
    result = [0, 1, 1]
    if n < 3:
        return result[n]
    while n - 2 > 0:
        result.append((result[1] + result[2]) % BASE)
        result.pop(0)
        n -= 1
    return result[-1]


fib(2)
fib(5)

