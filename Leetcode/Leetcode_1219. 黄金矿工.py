"""
1219. 黄金矿工
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。
每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
为了使收益最大化，矿工需要按以下规则来开采黄金：
每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
"""
from typing import List


def getMaximumGold(grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = 0

    def dfs(currentX, currentY, currentValue):
        nonlocal result
        result = max(result, currentValue)
        temp = grid[currentX][currentY]
        grid[currentX][currentY] = 0
        for direction in directions:
            nextX = currentX + direction[0]
            nextY = currentY + direction[1]
            if 0 <= nextX < row and 0 <= nextY < col and grid[nextX][nextY] != 0:
                dfs(nextX, nextY, currentValue + grid[nextX][nextY])
        grid[currentX][currentY] = temp

    for i in range(row):
        for j in range(col):
            if grid[i][j] != 0:
                dfs(i, j, grid[i][j])
    return result



