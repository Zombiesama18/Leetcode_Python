"""
539. 最小时间差
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
"""
from typing import List


def findMinDifference(timePoints: List[str]) -> int:
    timePoints = list(map(lambda x: int(x.split(':')[0]) * 24 + int(x.split(':')[1]), timePoints))
    timePoints.sort()
    minDifference = float('INF')
    for i in range(len(timePoints) - 1):
        if timePoints[i + 1] - timePoints[i] < minDifference:
            minDifference = timePoints[i + 1] - timePoints[i]
    minDifference = min(timePoints[0] + 1440 - timePoints[-1], minDifference)
    return minDifference


