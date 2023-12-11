"""
5965. 相同元素的间隔之和
给你一个下标从 0 开始、由 n 个整数组成的数组 arr 。
arr 中两个元素的 间隔 定义为它们下标之间的 绝对差 。更正式地，arr[i] 和 arr[j] 之间的间隔是 |i - j| 。
返回一个长度为 n 的数组 intervals ，其中 intervals[i] 是 arr[i] 和 arr 中每个相同元素（与 arr[i] 的值相同）的 间隔之和 。
"""
import collections
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        distribution = collections.defaultdict(list)
        for i, num in enumerate(arr):
            distribution[num].append(i)
        result = [0 for _ in range(len(arr))]
        for num in distribution:
            # 滚动求间隔和
            init_result = sum(x - distribution[num][0] for x in distribution[num])
            result[distribution[num][0]] = init_result

            for i in range(1, len(distribution[num])):
                left = i - 1  # 有left个间隔变大
                right = len(distribution[num]) - 1 - i  # 有right个间隔变小
                init_result += (left - right) * (distribution[num][i] - distribution[num][i - 1])
                result[distribution[num][i]] = init_result
        return result
