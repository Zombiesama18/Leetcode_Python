"""
1380. 矩阵中的幸运数
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
幸运数是指矩阵中满足同时下列两个条件的元素：
在同一行的所有元素中最小
在同一列的所有元素中最大
"""
from typing import *


def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    row, col = len(matrix), len(matrix[0])
    luckyNumberRow, luckyNumberCol = [float('INF')] * row, [0] * col
    for i in range(row):
        for j in range(col):
            luckyNumberRow[i] = min(luckyNumberRow[i], matrix[i][j])
            luckyNumberCol[j] = max(luckyNumberCol[j], matrix[i][j])
    result = list(set(luckyNumberRow).intersection(set(luckyNumberCol)))
    return result


luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
