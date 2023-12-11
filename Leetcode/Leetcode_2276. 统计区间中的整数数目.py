"""
2276. 统计区间中的整数数目
给你区间的 空 集，请你设计并实现满足要求的数据结构：
新增：添加一个区间到这个区间集合中。
统计：计算出现在 至少一个 区间中的整数个数。
实现 CountIntervals 类：
CountIntervals() 使用区间的空集初始化对象
void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
int count() 返回出现在 至少一个 区间中的整数个数。
注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。
"""

# 用 sortedcontainers 的 SortedDict 存右区间
import sortedcontainers


class CountIntervals:

    def __init__(self):
        self.dictionary = sortedcontainers.SortedDict()
        self.counter = 0

    def add(self, left: int, right: int) -> None:
        index = self.dictionary.bisect_left(left)
        while index < len(self.dictionary) and self.dictionary.values()[index] <= right:
            rBoundSection, lBoundSection = self.dictionary.items()[index]
            left = min(left, lBoundSection)
            right = max(right, rBoundSection)
            self.counter -= rBoundSection - lBoundSection + 1
            self.dictionary.popitem(index)
        self.counter += right - left + 1
        self.dictionary[right] = left

    def count(self) -> int:
        return self.counter


countIntervals = CountIntervals()
countIntervals.add(2, 3)
countIntervals.add(7, 10)
countIntervals.count()
countIntervals.add(5, 8)
countIntervals.count()

