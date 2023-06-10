"""
1072. 按列翻转得到最大值等行数

给定 m x n 矩阵 matrix 。
你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。
"""
import collections
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = collections.Counter()
        for row in matrix:
            if row[0] == 1:
                for j in range(len(row)):
                    row[j] ^= 1
            counter[tuple(row)] += 1
        return max(counter.values())

