# encoding = 'utf-8'
# 279. 完全平方数
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
import math


def numSquares(n: int) -> int:
    resultSequence = [float('INF')] * (n + 1)
    resultSequence[0] = 0
    baseList = []
    base = 0
    counter = 1
    while counter <= n:
        if counter == (base + 1) ** 2:
            base = base + 1
            baseList.insert(0, base ** 2)
            resultSequence[counter] = 1
        else:
            for bases in baseList:
                resultSequence[counter] = min(resultSequence[counter],
                                              resultSequence[counter - bases] + resultSequence[bases])
        counter += 1
    return resultSequence[-1]


numSquares(12)
numSquares(13)
