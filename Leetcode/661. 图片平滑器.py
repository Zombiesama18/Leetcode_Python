"""
661. 图片平滑器
图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
给你一个表示图像灰度的 m x n 整数矩阵 img ，返回对图像的每个单元格平滑处理后的图像 。
"""
from typing import List


def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (0, 0), (1, -1), (1, 0), (1, 1)]
    result = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            tempCounter, tempSum = 0, 0
            for stepX, stepY in directions:
                nextX, nextY = i + stepX, j + stepY
                if 0 <= nextX < len(img) and 0 <= nextY < len(img[0]):
                    tempCounter += 1
                    tempSum += img[nextX][nextY]
            result[i][j] = tempSum // tempCounter
    return result

