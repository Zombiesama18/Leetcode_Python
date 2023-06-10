"""
1637. 两点之间不包含任何点的最宽垂直区域

给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直区域 的宽度。
垂直区域 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直区域 为宽度最大的一个垂直区域。
请注意，垂直区域 边上 的点 不在 区域内。
"""
from typing import List


def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
    return max(y[0] - x[0] for x, y in zip(sorted(points, key=lambda x: x[0])[: -1],
                                           sorted(points, key=lambda x: x[0])[1:]))
