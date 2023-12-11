"""
497. 非重叠矩形中的随机点
给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，
(xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。
所有满足要求的点必须等概率被返回。
在给定的矩形覆盖的空间内的任何整数点都有可能被返回。
请注意 ，整数点是具有整数坐标的点。
实现 Solution 类:
Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。
"""
import bisect
import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for x1, y1, x2, y2 in rects:
            self.sum.append(self.sum[-1] + (x2 - x1 + 1) * (y2 - y1 + 1))

    def pick(self) -> List[int]:
        pointIndex = random.randint(0, self.sum[-1] - 1)
        rectIndex = bisect.bisect_right(self.sum, pointIndex) - 1
        x1, y1, x2, y2 = self.rects[rectIndex]
        offsetX, offsetY = divmod(pointIndex - self.sum[rectIndex], y2 - y1 + 1)
        return [x1 + offsetX, y1 + offsetY]
