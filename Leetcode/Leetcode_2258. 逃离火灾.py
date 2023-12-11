"""
2258. 逃离火灾

给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：
0 表示草地。
1 表示着火的格子。
2 表示一座墙，你跟火都不能通过这个格子。
一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。
每一分钟，你可以移动到 相邻 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。
请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。
如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 109 。
注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。
如果两个格子有共同边，那么它们为 相邻 格子。
"""
import collections
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        earliest_burning = [[-2 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    earliest_burning[i][j] = 0
                elif grid[i][j] == 2:
                    earliest_burning[i][j] = -1
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if earliest_burning[i][j] == 0:
                    q.append((i, j))
        time = 1
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            temp = []
            for current_pos_x, current_pos_y in q:
                for offset_x, offset_y in self.directions:
                    next_x, next_y = current_pos_x + offset_x, current_pos_y + offset_y
                    if (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and
                            earliest_burning[next_x][next_y] == -2):
                        earliest_burning[next_x][next_y] = time
                        temp.append((next_x, next_y))
            time += 1
            q = temp
        earliest_arrival = [[-2 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        earliest_arrival[0][0] = 0
        q = [(0, 0)]
        time = 1
        while q:
            temp = []
            for current_pos_x, current_pos_y in q:
                for offset_x, offset_y in self.directions:
                    next_x, next_y = current_pos_x + offset_x, current_pos_y + offset_y
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 0:
                        if earliest_arrival[next_x][next_y] == -2:
                            earliest_arrival[next_x][next_y] = time
                            temp.append((next_x, next_y))
            time += 1
            q = temp
        if earliest_arrival[-1][-1] == -2:
            return -1
        if earliest_burning[-1][-1] == -2:
            return 10 ** 9
        if earliest_burning[-1][-1] - earliest_arrival[-1][-1] < 0:
            return -1
        if earliest_arrival[-2][-1] != -2 and earliest_burning[-2][-1] - earliest_arrival[-2][-1] > \
                earliest_burning[-1][-1] - earliest_arrival[-1][-1] or \
                earliest_arrival[-1][-2] != -2 and earliest_burning[-1][-2] - earliest_arrival[-1][-2] > \
                earliest_burning[-1][-1] - earliest_arrival[-1][-1]:
            return earliest_burning[-1][-1] - earliest_arrival[-1][-1]
        return earliest_burning[-1][-1] - earliest_arrival[-1][-1] - 1


Solution().maximumMinutes([[0,0,2,2,1,1,0,2,1,1,2,2,0,2,2,1,2,0,1,2,2,0,1,2,2,1,2,2],[2,2,2,1,1,2,2,1,2,0,1,1,1,2,2,1,1,0,2,2,2,0,1,0,1,2,2,2],[0,0,1,1,0,1,2,0,1,1,1,1,0,2,0,2,0,2,1,1,0,2,1,2,2,2,1,2],[2,2,0,0,0,0,1,0,1,0,2,0,1,0,2,0,0,1,2,1,0,1,1,1,2,0,2,0],[2,2,1,1,1,1,1,0,0,0,0,2,0,1,1,1,1,2,0,2,1,1,2,0,2,0,2,0],[0,1,0,1,2,2,2,0,2,0,2,2,1,2,0,0,1,0,2,0,2,0,1,2,2,0,2,0],[1,0,2,2,2,0,2,0,2,0,2,0,1,0,2,2,0,2,1,1,1,0,1,0,1,1,0,0],[0,1,2,0,1,0,1,0,2,1,2,0,1,1,1,1,0,1,1,0,0,2,0,1,0,1,0,2],[2,1,1,0,1,1,2,2,1,2,2,1,0,1,0,0,0,2,1,0,2,2,1,2,1,2,0,1],[1,1,2,0,2,2,1,2,0,2,1,1,0,0,0,2,2,2,2,1,2,2,0,2,1,1,2,0],[2,1,2,2,0,0,1,0,1,2,1,0,1,0,2,0,0,1,1,0,2,0,2,0,1,2,2,0],[1,0,1,1,0,0,0,0,0,1,0,2,0,2,1,2,1,1,0,1,0,0,2,1,2,1,0,2],[2,0,1,0,2,0,1,0,2,0,2,1,2,0,2,2,2,1,0,2,1,0,1,2,1,0,1,1],[0,2,2,1,0,2,1,0,1,2,2,1,2,2,1,2,0,1,2,2,0,2,1,0,2,1,0,0],[0,2,2,2,1,2,1,0,0,2,2,0,1,0,2,1,0,0,2,1,1,1,2,1,2,1,0,1],[2,2,2,1,1,1,1,0,2,2,2,1,0,0,2,2,0,0,1,1,0,0,2,1,2,1,2,2],[2,1,2,1,1,1,0,2,1,0,1,1,2,1,0,0,1,1,2,1,2,2,1,2,0,2,0,0]])
