"""
729. 我的日程安排表 I
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end 。
实现 MyCalendar 类：
MyCalendar() 初始化日历对象。
boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。
否则，返回 false 并且不要将该日程安排添加到日历中。
"""
import sortedcontainers


class MyCalendar:

    def __init__(self):
        self.queue = sortedcontainers.SortedDict()

    def book(self, start: int, end: int) -> bool:
        index = self.queue.bisect_left(end)
        if index == 0 or self.queue.items()[index - 1][1] <= start:
            self.queue[start] = end
            return True
        return False
