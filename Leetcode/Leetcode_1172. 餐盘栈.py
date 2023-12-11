"""
1172. 餐盘栈

我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。

实现一个叫「餐盘」的类 DinnerPlates：
DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
"""
import collections
import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []
        self.empty = []
        self.stack_volume = collections.defaultdict(int)

    def push(self, val: int) -> None:
        if not self.empty:
            self.data.append(val)
            stack_idx = (len(self.data) - 1) // self.capacity
            self.stack_volume[stack_idx] += 1
        else:
            idx_to_insert = heapq.heappop(self.empty)
            if idx_to_insert >= len(self.data):
                self.empty = []
                self.push(val)
            else:
                self.data[idx_to_insert] = val
                self.stack_volume[idx_to_insert // self.capacity] += 1

    def pop(self) -> int:
        while self.data and self.data[-1] == -1:
            self.data.pop(-1)
        if not self.data:
            return -1
        self.stack_volume[(len(self.data) - 1) // self.capacity] -= 1
        return self.data.pop(-1)

    def popAtStack(self, index: int) -> int:
        if self.stack_volume[index] == 0:
            return -1
        self.stack_volume[index] -= 1
        idx_to_pop = index * self.capacity + self.stack_volume[index]
        heapq.heappush(self.empty, idx_to_pop)
        result = self.data[idx_to_pop]
        self.data[idx_to_pop] = -1
        return result


D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
D.popAtStack(0)
D.push(20)
D.push(21)
D.popAtStack(0)
D.popAtStack(2)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()
