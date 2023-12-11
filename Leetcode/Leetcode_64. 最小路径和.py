# 64. 最小路径和
# 给定一个包含非负整数的 m x n1 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。


def minPathSum(grid):
    output = []
    finish = [len(grid) - 1, len(grid[0]) - 1]

    def recursion(now, direction, distance):
        temp = [now[0] + direction[0], now[1] + direction[1]]
        if temp == finish:
            output.append(distance + grid[-1][-1])
            return
        if temp[0] < finish[0]:
            recursion(temp, [1, 0], distance + grid[temp[0]][temp[1]])
        if temp[1] < finish[1]:
            recursion(temp, [0, 1], distance + grid[temp[0]][temp[1]])

    recursion([0, 0], [1, 0], grid[0][0])
    recursion([0, 0], [0, 1], grid[0][0])
    return min(output)


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
minPathSum(grid)
