"""
2661. 找出叠涂元素

给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数。
从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。
请你找出 arr 中在 mat 的某一行或某一列上都被涂色且下标最小的元素，并返回其下标 i 。
"""
import collections
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        item_2_row_col = collections.defaultdict(tuple)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row_dict[i].add(mat[i][j])
                col_dict[j].add(mat[i][j])
                item_2_row_col[mat[i][j]] = (i, j)
        for i, num in enumerate(arr):
            row, col = item_2_row_col[num]
            row_dict[row].remove(num)
            if not row_dict[row]:
                return i
            col_dict[col].remove(num)
            if not col_dict[col]:
                return i


