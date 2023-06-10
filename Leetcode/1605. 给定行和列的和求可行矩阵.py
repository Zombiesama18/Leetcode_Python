"""
1605. 给定行和列的和求可行矩阵

给你两个非负整数数组 rowSum 和 colSum ，其中 rowSum[i] 是二维矩阵中第 i 行元素的和， colSum[j] 是第 j 列元素的和。
换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。
请找到大小为 rowSum.length x colSum.length 的任意 非负整数 矩阵，且该矩阵满足 rowSum 和 colSum 的要求。
请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个 可行矩阵。
"""
from typing import List


def restoreMatrix(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    result = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

    sorted_row = list(sorted([[i, v] for i, v in enumerate(rowSum)], key=lambda x: x[1]))
    sorted_col = list(sorted([[i, v] for i, v in enumerate(colSum)], key=lambda x: x[1]))

    while sorted_row and sorted_col:
        if sorted_row and sorted_col:
            min_value = min(sorted_row[0][1], sorted_col[0][1])
            result[sorted_row[0][0]][sorted_col[0][0]] = min_value
            if sorted_row[0][1] == min_value:
                sorted_row.pop(0)
            else:
                sorted_row[0][1] -= min_value
            if sorted_col[0][1] == min_value:
                sorted_col.pop(0)
            else:
                sorted_col[0][1] -= min_value
    return result


restoreMatrix(rowSum = [3,8], colSum = [4,7])

