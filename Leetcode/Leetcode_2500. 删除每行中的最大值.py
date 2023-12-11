"""
2500. 删除每行中的最大值

给你一个 m x n 大小的矩阵 grid ，由若干正整数组成。
执行下述操作，直到 grid 变为空矩阵：
从每一行删除值最大的元素。如果存在多个这样的值，删除其中任何一个。
将删除元素中的最大值与答案相加。
注意 每执行一次操作，矩阵中列的数据就会减 1 。
返回执行上述操作后的答案。
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        result = 0
        for i in range(len(grid[0])):
            result += max([grid[j].pop() for j in range(len(grid))])
        return result
