"""
1090. 受标签影响的最大值

我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。
还会给出两个整数 numWanted 和 useLimit 。
从 n 个元素中选择一个子集 s :
子集 s 的大小 小于或等于 numWanted 。
s 中 最多 有相同标签的 useLimit 项。
一个子集的 分数 是该子集的值之和。
返回子集 s 的最大 分数 。
"""
import collections
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        label_dict = collections.defaultdict(list)
        for label, value in zip(labels, values):
            label_dict[label].append(value)
        for k, v in label_dict.items():
            label_dict[k] = list(sorted(v, reverse=True))
        candidates = []
        for k, v in label_dict.items():
            candidates.extend(v[:useLimit])
        return sum(list(sorted(candidates, reverse=True))[:numWanted])


