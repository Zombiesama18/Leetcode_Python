"""
2013. 检测正方形
给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。
实现 DetectSquares 类：
DetectSquares() 使用空数据结构初始化对象
void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
"""
import collections
from typing import *


class DetectSquares:

    def __init__(self):
        self.rowDict = collections.defaultdict(set)
        self.pointDict = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.rowDict[point[0]].add(point[1])
        self.pointDict[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        counter = 0
        for col in self.rowDict[point[0]]:
            if col == point[1]:
                continue
            possibleRow = [point[0] + col - point[1], point[0] - col + point[1]]
            for row in possibleRow:
                if (row, col) in self.pointDict and (row, point[1]) in self.pointDict:
                    counter += self.pointDict[(point[0], col)] * self.pointDict[(row, col)] * \
                               self.pointDict[(row, point[1])]
        return counter


s = DetectSquares()
s.add([3, 10])
s.add([11, 2])
s.add([3, 2])
s.count([11, 10])
s.count([14, 8])
s.add([11, 2])
s.count([11, 10])
