"""
436. 寻找右区间
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。
返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。
"""
import bisect
from typing import List


def findRightInterval(intervals: List[List[int]]) -> List[int]:
    dictionary = {start: i for i, (start, end) in enumerate(intervals)}
    result = [-1] * len(intervals)
    rightSideDict = {}
    starts = list(sorted([start for start, end in intervals]))
    for i, (start, end) in enumerate(intervals):
        if end not in rightSideDict:
            if end <= starts[0]:
                targetIndex = dictionary[starts[0]]
                result[i] = targetIndex
                rightSideDict[end] = targetIndex
            elif end <= starts[-1]:
                targetIndex = dictionary[starts[bisect.bisect_left(starts, end)]]
                result[i] = targetIndex
                rightSideDict[end] = targetIndex
            else:
                rightSideDict[end] = -1
        else:
            result[i] = rightSideDict[end]
    return result




