# 5877. 检测正方形（需要复习）
# 给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
# 添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
# 给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
# 轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。
# 实现 DetectSquares 类：
# DetectSquares() 使用空数据结构初始化对象
# void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
# int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
import collections


class DetectSquares:

    def __init__(self):
        self.rowDict = collections.defaultdict(list)
        self.colDict = collections.defaultdict(list)
        self.pointSet = set()

    def add(self, point: [int]) -> None:
        self.rowDict[point[0]].append(point[1])
        self.colDict[point[1]].append(point[0])
        self.pointSet.add(tuple(point))

    def count(self, point: [int]) -> int:
        counter = 0
        for possibleRow in self.colDict[point[1]]:
            for possibleCol in self.rowDict[point[0]]:
                if (possibleRow, possibleCol) in self.pointSet:
                    counter += 1
        return counter


detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
detectSquares.count([11, 10])
detectSquares.count([14, 8])
detectSquares.add([11, 2])
detectSquares.count([11, 10])





