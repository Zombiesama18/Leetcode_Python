"""
5976. 检查是否每一行每一列都包含全部整数
对一个大小为 n x n 的矩阵而言，如果其每一行和每一列都包含从 1 到 n 的 全部 整数（含 1 和 n），则认为该矩阵是一个 有效 矩阵。
给你一个大小为 n x n 的整数矩阵 matrix ，请你判断矩阵是否为一个有效矩阵：如果是，返回 true ；否则，返回 false 。
"""
from typing import List


def checkValid(matrix: List[List[int]]) -> bool:
    listSetRow = [set() for _ in range(len(matrix))]
    listSetCol = [set() for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in listSetRow[i] or matrix[i][j] in listSetCol[j]:
                return False
            listSetRow[i].add(matrix[i][j])
            listSetCol[j].add(matrix[i][j])
    return True


checkValid([[1,2,3],[3,1,2],[2,3,1]])


