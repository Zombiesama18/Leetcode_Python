"""
2280. 表示一个折线图的最少线段数
给你一个二维整数数组 stockPrices ，其中 stockPrices[i] = [dayi, pricei] 表示股票在 dayi 的价格为 pricei 。
折线图 是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。

请你返回要表示一个折线图所需要的 最少线段数 。
"""
import math
from typing import List


def minimumLines(stockPrices: List[List[int]]) -> int:
    if len(stockPrices) == 1:
        return 1
    stockPrices.sort(key=lambda x: x[0])
    dy = stockPrices[1][1] - stockPrices[0][1]
    dx = stockPrices[1][0] - stockPrices[0][0]
    gcdNumber = math.gcd(dy, dx)
    lastSlope = (dy // gcdNumber, dx // gcdNumber)
    result = 1
    for i in range(1, len(stockPrices) - 1):
        dy = stockPrices[i + 1][1] - stockPrices[i][1]
        dx = stockPrices[i + 1][0] - stockPrices[i][0]
        gcdNumber = math.gcd(dy, dx)
        thisSlope = (dy // gcdNumber, dx // gcdNumber)
        if lastSlope != thisSlope:
            lastSlope = thisSlope
            result += 1
    return result

