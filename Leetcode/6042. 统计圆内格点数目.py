"""
6042. 统计圆内格点数目
给你一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示网格上圆心为 (xi, yi) 且半径为 ri 的第 i 个圆，
返回出现在 至少一个 圆内的 格点数目 。
注意：
格点 是指整数坐标对应的点。
圆周上的点 也被视为出现在圆内的点。
"""
import math
from typing import List


def countLatticePoints(circles: List[List[int]]) -> int:
    result = set()
    for circle in circles:
        for x in range(circle[0] - circle[2], circle[0] + circle[2] + 1):
            for y in range(circle[1] - circle[2], circle[1] + circle[2] + 1):
                if math.sqrt((x - circle[0]) ** 2 + (y - circle[1]) ** 2) <= circle[2]:
                    result.add((x, y))
    return len(result)


def countLatticePointsQuicker(circles: List[List[int]]) -> int:
    result = 0
    maxX, minX, maxY, minY = float('-INF'), float('INF'), float('-INF'), float('INF')
    for circle in circles:
        maxX = max(maxX, circle[0] + circle[2])
        minX = min(minX, circle[0] - circle[2])
        maxY = max(maxY, circle[1] + circle[2])
        minY = min(minY, circle[1] - circle[2])
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            for circle in circles:
                if math.sqrt((x - circle[0]) ** 2 + (y - circle[1]) ** 2) <= circle[2]:
                    result += 1
                    break
    return result

