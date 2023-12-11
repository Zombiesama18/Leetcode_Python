import collections


# 200. 岛屿数量（需要复习）
# 给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
# 用一个等大的矩阵来表示有没有访问过
def numIslands(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                grid[i][j] = '0'  # 表示访问过
                counter += 1
                land_posits = collections.deque()
                land_posits.append([i, j])
                while len(land_posits) > 0:  # 遍历出一整块陆地
                    x, y = land_posits.popleft()
                    for new_x, new_y in ([x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]):
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                            # 如果新的xy在grid里而且对应地点也是陆地
                            grid[new_x][new_y] = '0'
                            land_posits.append([new_x, new_y])
    return counter


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
numIslands(grid)
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
numIslands(grid)
