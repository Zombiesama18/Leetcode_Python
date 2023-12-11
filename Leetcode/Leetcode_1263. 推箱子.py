"""
1263. 推箱子

「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
地板用字符 '.' 表示，意味着可以自由行走。
墙用字符 '#' 表示，意味着障碍物，不能通行。 
箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
玩家无法越过箱子。
返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。
"""
import collections
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        p_x, p_y, b_x, b_y = None, None, None, None
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 'S':
                    p_x = i
                    p_y = j
                elif grid[i][j] == 'B':
                    b_x = i
                    b_y = j
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        states = [[float('inf')] * (self.m * self.n) for _ in range(self.m * self.n)]
        states[p_x * self.n + p_y][b_x * self.n + b_y] = 0
        q = collections.deque([(p_x * self.n + p_y, b_x * self.n + b_y)])
        while q:
            q1 = collections.deque()
            while q:
                s1, b1 = q.popleft()
                sx1, sy1 = s1 // self.n, s1 % self.n
                bx1, by1 = b1 // self.n, b1 % self.n
                if grid[bx1][by1] == 'T':
                    return states[s1][b1]
                for offset_x, offset_y in directions:
                    sx2, sy2 = sx1 + offset_x, sy1 + offset_y
                    s2 = sx2 * self.n + sy2
                    if not self.check_valid(sx2, sy2):
                        continue
                    if sx2 == bx1 and sy2 == by1:
                        bx2, by2 = bx1 + offset_x, by1 + offset_y
                        b2 = bx2 * self.n + by2
                        if not self.check_valid(bx2, by2) or states[s2][b2] <= states[s1][b1] + 1:
                            continue
                        states[s2][b2] = states[s1][b1] + 1
                        q1.append((s2, b2))
                    else:
                        if states[s2][b1] <= states[s1][b1]:
                            continue
                        states[s2][b1] = states[s1][b1]
                        q.append((s2, b1))
            q, q1 = q1, q
        return -1

    def check_valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] != '#'


Solution().minPushBox(grid = [["#","#","#","#","#","#"], ["#","T","#","#","#","#"], ["#",".",".","B",".","#"],
                      ["#",".","#","#",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]])

