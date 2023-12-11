"""
498. 对角线遍历
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
"""
from typing import List


def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    direction = True
    result = []
    targetNumbers = len(mat) * len(mat[0])
    indexX, indexY = 0, 0
    while len(result) < targetNumbers:
        result.append(mat[indexX][indexY])
        if direction:
            if indexY == len(mat[0]) - 1:
                indexX += 1
                direction = not direction
            elif indexX == 0:
                indexY += 1
                direction = not direction
            else:
                indexX -= 1
                indexY += 1
        else:
            if indexX == len(mat) - 1:
                indexY += 1
                direction = not direction
            elif indexY == 0:
                indexX += 1
                direction = not direction
            else:
                indexX += 1
                indexY -= 1
    return result


findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])

