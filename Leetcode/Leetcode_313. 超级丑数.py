# 313. 超级丑数
# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
import heapq


def nthSuperUglyNumber(n: int, primes: [int]) -> int:
    addedNumber = {1}
    heap = [1]
    for i in range(n):
        ugly = heapq.heappop(heap)
        for prime in primes:
            nextUgly = ugly * prime
            if nextUgly not in addedNumber:
                addedNumber.add(nextUgly)
                heapq.heappush(heap, nextUgly)
    return ugly


nthSuperUglyNumber(12, [2,7,13,19])


