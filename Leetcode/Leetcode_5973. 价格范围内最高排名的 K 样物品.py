"""
5973. 价格范围内最高排名的 K 样物品
给你一个下标从 0    开始的二维整数数组    grid    ，它的大小为    m x n    ，表示一个商店中物品的分布图。数组中的整数含义为：
0    表示无法穿越的一堵墙。
1    表示可以自由通过的一个空格子。
所有其他正整数表示该格子内的一样物品的价格。你可以自由经过这些格子。
从一个格子走到上下左右相邻格子花费    1    步。
同时给你一个整数数组    pricing 和    start    ，其中    pricing = [low, high] 且    start = [row, col]    ，
表示你开始位置为    (row, col)    ，同时你只对物品价格在    闭区间    [low, high]    之内的物品感兴趣。同时给你一个整数    k    。
你想知道给定范围 内    且 排名最高    的 k    件物品的 位置    。排名按照优先级从高到低的以下规则制定：
距离：定义为从    start    到一件物品的最短路径需要的步数（较近    距离的排名更高）。
价格：较低    价格的物品有更高优先级，但只考虑在给定范围之内的价格。
行坐标：较小    行坐标的有更高优先级。
列坐标：较小    列坐标的有更高优先级。
请你返回给定价格内排名最高的 k    件物品的坐标，将它们按照排名排序后返回。如果给定价格内少于 k    件物品，那么请将它们的坐标    全部    返回。
"""
import collections
from typing import *


def highestRankedKItems(grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    result = []
    row, col = len(grid), len(grid[0])
    visited = {(start[0], start[1])}
    q = collections.deque([(start[0], start[1], 0)])
    while q:
        currentX, currentY, step = q.popleft()
        if grid[currentX][currentY] != 1 and pricing[0] <= grid[currentX][currentY] <= pricing[1]:
            result.append([currentX, currentY, step])
            if len(result) == 2 * k:
                break
        for direction in directions:
            nextX, nextY = currentX + direction[0], currentY + direction[1]
            if 0 <= nextX < row and 0 <= nextY < col and grid[nextX][nextY] != 0 and (nextX, nextY) not in visited:
                visited.add((nextX, nextY))
                q.append((nextX, nextY, step + 1))
    result.sort(key=lambda x: (x[2], grid[x[0]][x[1]], x[0], x[1]))
    output = [[result[i][0], result[i][1]] for i in range(min(k, len(result)))]
    return output


highestRankedKItems([[1,2,0,1],[1,3,0,1],[0,2,5,1]], [2,5], [0,0], 3)
highestRankedKItems([[1,0,1],[3,5,2],[1,0,1]], [2,5], [1,1], 9)
