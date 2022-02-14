"""
24. 机器人的运动范围
地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。
一个机器人从坐标 (0,0) 的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。
但是不能进入行坐标和列坐标的数位之和大于 k 的格子。
请问该机器人能够达到多少个格子？
"""


def movingCount(threshold, rows, cols):
    """
    :type threshold: int
    :type rows: int
    :type cols: int
    :rtype: int
    """

    def dfs(currentX, currentY):
        if not 0 <= currentX < rows or not 0 <= currentY < cols or (currentX, currentY) in visited or \
                sum([int(number1) for number1 in str(currentX)] + [int(number2) for number2 in
                                                                   str(currentY)]) > threshold:
            return
        nonlocal counter
        counter += 1
        visited.add((currentX, currentY))
        for stepX, stepY in directions:
            dfs(currentX + stepX, currentY + stepY)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    counter = 0
    visited = set()
    dfs(0, 0)
    return counter


movingCount(9, 20, 25)
