# 149. 直线上最多的点数
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
from fractions import Fraction


def maxPoints(points: [[int]]) -> int:
    length = len(points)
    if length < 2:
        return length
    lineSet = {}
    for i in range(1, length):
        for j in range(0, i):
            if points[i][0] == points[j][0]:
                lineProperty = (points[i][0], float('INF'))
                if lineProperty in lineSet:
                    if points[i][1] not in lineSet[lineProperty][1]:
                        lineSet[lineProperty][0] += 1
                        lineSet[lineProperty][1].add(points[i][1])
                else:
                    lineSet[lineProperty] = [2, {points[i][1], points[j][1]}]
            else:
                slope = Fraction(points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                lineProperty = (slope, points[i][1] - slope * points[i][0])
                if lineProperty in lineSet:
                    if points[i][0] not in lineSet[lineProperty][1]:
                        lineSet[lineProperty][0] += 1
                        lineSet[lineProperty][1].add(points[i][0])
                else:
                    lineSet[lineProperty] = [2, {points[i][0], points[j][0]}]
    maxNumber = 0
    for line in lineSet:
        maxNumber = max(maxNumber, lineSet[line][0])
    return maxNumber


maxPoints([[1,1],[2,2],[3,3]])
maxPoints([[-6,-1],[3,1],[12,3]])

