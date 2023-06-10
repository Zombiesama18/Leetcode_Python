"""
2352. 相等行列对

给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。

如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
"""
import collections
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter, col_counter = collections.Counter(), collections.Counter()
        for i, row in enumerate(grid):
            row_counter[tuple(row)] += 1
            col = tuple([grid[j][i] for j in range(len(grid))])
            col_counter[col] += 1
        result = 0
        for row in row_counter:
            if row in col_counter:
                result += row_counter[row] * col_counter[row]
        return result

Solution().equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]])
