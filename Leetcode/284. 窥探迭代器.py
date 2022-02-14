# 284. 窥探迭代器
# 请你设计一个迭代器，除了支持 hasNext 和 next 操作外，还支持 peek 操作。
# 实现 PeekingIterator 类：
# PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
# int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
# bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
# int peek() 返回数组中的下一个元素，但 不 移动指针。
import collections
import queue


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.bufferQueue = collections.deque()
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.bufferQueue:
            if self.iterator.hasNext():
                self.bufferQueue.append(self.iterator.next())
        return self.bufferQueue[0]

    def next(self):
        """
        :rtype: int
        """
        if not self.bufferQueue:
            if self.iterator.hasNext():
                return self.iterator.next()
        else:
            return self.bufferQueue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.bufferQueue:
            if not self.iterator.hasNext():
                return False
        return True


p = PeekingIterator()



