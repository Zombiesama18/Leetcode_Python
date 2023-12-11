"""
1439. 有序矩阵中的第 k 个最小数组和

给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
"""
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

