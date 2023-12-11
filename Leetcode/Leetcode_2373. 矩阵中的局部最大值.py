"""
2373. 矩阵中的局部最大值

给你一个大小为 n x n 的整数矩阵 grid 。
生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：
maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。
返回生成的矩阵。
"""
from typing import List


def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    result = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]

    def traverse(num_seq, current_i, current_j):
        num_seq.pop(0)
        num_seq.pop(2)
        num_seq.pop(4)
        num_seq.insert(2, grid[current_i - 1][current_j + 1])
        num_seq.insert(5, grid[current_i][current_j + 1])
        num_seq.insert(8, grid[current_i + 1][current_j + 1])
        max_value = max(num_seq)
        result[current_i - 1][current_j - 1] = max_value
        if current_j < len(grid) - 2:
            traverse(num_seq, current_i, current_j + 1)

    num_seq = [0, 0, 0]
    num_seq.extend(grid[0][:3])
    num_seq.extend(grid[1][:3])
    for i in range(1, len(grid) - 1):
        num_seq.pop(0)
        num_seq.pop(0)
        num_seq.pop(0)
        num_seq.extend(grid[i + 1][:3])
        result[i - 1][0] = max(num_seq)
        if len(grid) > 3:
            temp = num_seq[:]
            traverse(num_seq, i, 2)
            num_seq = temp
    return result


largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
