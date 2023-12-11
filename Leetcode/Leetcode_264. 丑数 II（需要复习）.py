# 264. 丑数 II（需要复习）
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
import heapq


def nthUglyNumber(n: int) -> int:
    uglyNumbers = {1}
    multiplier2 = 1
    multiplier3 = 1
    multiplier5 = 1
    while len(uglyNumbers) < n:
        if 2 * multiplier2 < 3 * multiplier3:
            if multiplier2 in uglyNumbers:
                uglyNumbers.add(2 * multiplier2)
            multiplier2 += 1
        elif 3 * multiplier3 < 5 * multiplier5:
            if multiplier3 in uglyNumbers:
                uglyNumbers.add(3 * multiplier3)
            multiplier3 += 1
        else:
            if multiplier5 in uglyNumbers:
                uglyNumbers.add(5 * multiplier5)
            multiplier5 += 1
    result = list(uglyNumbers)
    result.sort()
    return result[n - 1]


ns = [10, 1, 38]
for n in ns:
    print('输入：{}\t结果：{}'.format(n, nthUglyNumber(n)))


def nthUglyNumberDynamicPlanning(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    pointer2, pointer3, pointer5 = 1, 1, 1
    for i in range(2, n + 1):
        number2, number3, number5 = 2 * dp[pointer2], 3 * dp[pointer3], 5 * dp[pointer5]
        dp[i] = min(number2, number3, number5)
        if dp[i] == number2:
            pointer2 += 1
        if dp[i] == number3:
            pointer3 += 1
        if dp[i] == number5:
            pointer5 += 1
    return dp[n]


def nthUglyNumberMinHeap(n: int) -> int:
    multipliers = [2, 3, 5]
    heap = [1]
    uglyNumbers = {1}
    for i in range(n - 1):
        currentNumber = heapq.heappop(heap)
        for multiplier in multipliers:
            nextNumber = currentNumber * multiplier
            if nextNumber not in uglyNumbers:
                uglyNumbers.add(nextNumber)
                heapq.heappush(heap, nextNumber)
    return heapq.heappop(heap)


ns = [10, 1, 38]
for n in ns:
    print('输入：{}\t结果：{}'.format(n, nthUglyNumberMinHeap(n)))
