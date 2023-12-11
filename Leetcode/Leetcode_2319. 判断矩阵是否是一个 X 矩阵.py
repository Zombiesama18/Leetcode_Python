"""
2319. 判断矩阵是否是一个 X 矩阵
如果一个正方形矩阵满足下述 全部 条件，则称之为一个 X 矩阵 ：
矩阵对角线上的所有元素都 不是 0
矩阵中所有其他元素都是 0
给你一个大小为 n x n 的二维整数数组 grid ，表示一个正方形矩阵。如果 grid 是一个 X 矩阵 ，返回 true ；否则，返回 false 。
"""
from typing import List


def checkXMatrix(grid: List[List[int]]) -> bool:
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if i == j :
                if grid[i][j] == 0:
                    return False
            elif i + j == length - 1:
                if grid[i][j] == 0:
                    return False
            elif grid[i][j] != 0:
                return False
    return True


checkXMatrix(grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])


