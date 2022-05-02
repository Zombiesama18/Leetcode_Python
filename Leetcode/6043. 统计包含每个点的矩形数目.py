"""
6043. 统计包含每个点的矩形数目
给你一个二维整数数组 rectangles ，其中 rectangles[i] = [li, hi] 表示第 i 个矩形长为 li 高为 hi 。给你一个二维整数数组 points ，
其中 points[j] = [xj, yj] 是坐标为 (xj, yj) 的一个点。
第 i 个矩形的 左下角 在 (0, 0) 处，右上角 在 (li, hi) 。
请你返回一个整数数组 count ，长度为 points.length，其中 count[j]是 包含 第 j 个点的矩形数目。
如果 0 <= xj <= li 且 0 <= yj <= hi ，那么我们说第 i 个矩形包含第 j 个点。如果一个点刚好在矩形的 边上 ，这个点也被视为被矩形包含。
"""
import bisect
from typing import List


def countRectangles(rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
    rectangles.sort(key=lambda r: -r[1])
    result = [0] * len(points)
    index, xAxis = 0, []
    points = sorted([(x, y, i) for i, (x, y) in enumerate(points)], key=lambda r: -r[1])
    for x, y, i in points:
        flag = False
        while index < len(rectangles) and rectangles[index][1] >= y:
            xAxis.append(rectangles[index][0])
            index += 1
            flag = True
        if flag:
            xAxis.sort()
        result[i] = index - bisect.bisect_left(xAxis, x)
    return result


countRectangles(rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]])
