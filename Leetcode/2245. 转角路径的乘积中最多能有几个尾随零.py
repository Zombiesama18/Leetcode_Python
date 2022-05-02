"""
2245. 转角路径的乘积中最多能有几个尾随零
给你一个二维整数数组 grid ，大小为 m x n，其中每个单元格都含一个正整数。
转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），
而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；
反之亦然。当然，同样不能访问之前已经访问过的单元格。
一条路径的 乘积 定义为：路径上所有值的乘积。
请你从 grid 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。
注意：
水平 移动是指向左或右移动。
竖直 移动是指向上或下移动。
"""
from typing import List


def maxTrailingZeros(grid: List[List[int]]) -> int:
    factor2, factor5 = [0] * 1001, [0] * 1001
    for i in range(2, 1001):
        if i % 2 == 0:
            factor2[i] = factor2[i // 2] + 1
        if i % 5 == 0:
            factor5[i] = factor5[i // 5] + 1
    result = 0
    diff2, diff5 = [[0 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid))], \
                   [[0 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            diff2[i][j + 1] = diff2[i][j] + factor2[grid[i][j]]
            diff5[i][j + 1] = diff5[i][j] + factor5[grid[i][j]]
    for j in range(len(grid[0])):
        sumOf2 = sumOf5 = 0
        for i in range(len(grid)):
            sumOf2 += factor2[grid[i][j]]
            sumOf5 += factor5[grid[i][j]]
            result = max(result, max(min(sumOf2 + diff2[i][j], sumOf5 + diff5[i][j]),
                                     min(sumOf2 + diff2[i][-1] - diff2[i][j + 1],
                                         sumOf5 + diff5[i][-1] - diff5[i][j + 1])))
        sumOf2 = sumOf5 = 0
        for i in range(len(grid) - 1, -1, -1):
            sumOf2 += factor2[grid[i][j]]
            sumOf5 += factor5[grid[i][j]]
            result = max(result, max(min(sumOf2 + diff2[i][j], sumOf5 + diff5[i][j]),
                                     min(sumOf2 + diff2[i][-1] - diff2[i][j + 1],
                                         sumOf5 + diff5[i][-1] - diff5[i][j + 1])))
    return result
