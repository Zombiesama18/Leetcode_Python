"""
57. 插入区间

给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
"""
import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        left_insured = False
        left_starter, right_end = None, None
        for interval in intervals:
            if not left_insured:
                if newInterval[0] <= interval[1]:
                    left_insured = True
                    left_starter = min(newInterval[0], interval[0])
                else:
                    result.append(interval)
            if left_insured:
                if left_starter != float('inf'):
                    if interval[0] <= newInterval[1] <= interval[1]:
                        right_end = interval[1]
                        result.append([left_starter, right_end])
                        left_starter = float('inf')
                    elif newInterval[1] < interval[0]:
                        right_end = newInterval[1]
                        result.append([left_starter, right_end])
                        result.append(interval)
                        left_starter = float('inf')
                else:
                    result.append(interval)
        if left_starter is None:
            result.append(newInterval)
        elif right_end is None:
            result.append([left_starter, newInterval[1]])
        return result


Solution().insert(intervals = [[1,5]], newInterval = [0,0])

