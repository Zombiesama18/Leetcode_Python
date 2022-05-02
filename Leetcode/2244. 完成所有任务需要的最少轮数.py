"""
2244. 完成所有任务需要的最少轮数
给你一个下标从 0 开始的整数数组 tasks ，其中 tasks[i] 表示任务的难度级别。在每一轮中，你可以完成 2 个或者 3 个 相同难度级别 的任务。
返回完成所有任务需要的 最少 轮数，如果无法完成所有任务，返回 -1 。
"""
import collections
from typing import List


def minimumRounds(tasks: List[int]) -> int:
    taskDictionary = collections.Counter(tasks)
    result = 0
    for task, times in taskDictionary.items():
        if times == 1:
            return -1
        result += times // 3
        if times % 3 != 0:
            result += 1
    return result


minimumRounds([3,3])

