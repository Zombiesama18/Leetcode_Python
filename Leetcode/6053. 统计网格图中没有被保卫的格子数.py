"""
6053. 统计网格图中没有被保卫的格子数
给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，
其中 guards[i] = [rowi, coli] 且 walls[j] = [rowj, colj] ，分别表示第 i 个警卫和第 j 座墙所在的位置。
一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。
如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。
请你返回空格子中，有多少个格子是 没被保卫 的。
"""
from typing import List


def countUnguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    grids = [[1 for _ in range(n)] for _ in range(m)]

    def search(position: [int]):
        temp = [position[0], position[1] - 1]
        while temp[1] >= 0:
            if grids[temp[0]][temp[1]] == -1:
                break
            grids[temp[0]][temp[1]] = 0
            temp[1] -= 1
        temp = [position[0], position[1] + 1]
        while temp[1] < n:
            if grids[temp[0]][temp[1]] == -1:
                break
            grids[temp[0]][temp[1]] = 0
            temp[1] += 1
        temp = [position[0] - 1, position[1]]
        while temp[0] >= 0:
            if grids[temp[0]][temp[1]] == -1:
                break
            grids[temp[0]][temp[1]] = 0
            temp[0] -= 1
        temp = [position[0] + 1, position[1]]
        while temp[0] < m:
            if grids[temp[0]][temp[1]] == -1:
                break
            grids[temp[0]][temp[1]] = 0
            temp[0] += 1

    for wall in walls:
        grids[wall[0]][wall[1]] = -1
    for guard in guards:
        grids[guard[0]][guard[1]] = -1
    for guard in guards:
        search(guard)
    result = 0
    for i in range(m):
        for j in range(n):
            if grids[i][j] == 1:
                result += 1
    return result


countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])

