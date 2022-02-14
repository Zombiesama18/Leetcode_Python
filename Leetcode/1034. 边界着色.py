"""
1034. 边界着色
给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。
当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一 连通分量 。
连通分量的边界 是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。
请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。
"""
import copy


def colorBorder(grid: [[int]], row: int, col: int, color: int) -> [[int]]:
    change_set = set()
    visited = set()
    rows, cols = len(grid), len(grid[0])
    target_color = grid[row][col]

    def search(current_row, current_col, target):
        if grid[current_row][current_col] != target or (current_row, current_col) in visited:
            return
        visited.add((current_row, current_col))
        if is_border(current_row, current_col):
            change_set.add((current_row, current_col))
        if current_row > 0:
            search(current_row - 1, current_col, target)
        if current_row < rows - 1:
            search(current_row + 1, current_col, target)
        if current_col > 0:
            search(current_row, current_col - 1, target)
        if current_col < cols - 1:
            search(current_row, current_col + 1, target)

    def is_border(position_row, position_col):
        this_color = grid[position_row][position_col]
        if any((position_row == 0, position_row == rows - 1, position_col == 0, position_col == cols - 1)):
            return True
        return any((grid[position_row - 1][position_col] != this_color,
                    grid[position_row + 1][position_col] != this_color,
                    grid[position_row][position_col - 1] != this_color,
                    grid[position_row][position_col + 1] != this_color))

    search(row, col, target_color)
    for r, c in change_set:
        grid[r][c] = color
    return grid


colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2)

