"""
23. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
"""


def hasPath(matrix, string):
    """
    :type matrix: List[List[str]]
    :type string: str
    :rtype: bool
    """

    def search(currentX, currentY, index, visited):
        if index == len(string):
            return True
        for direction in directions:
            nextX, nextY = currentX + direction[0], currentY + direction[1]
            if 0 <= nextX < len(matrix) and 0 <= nextY < len(matrix[0]) and (nextX, nextY) not in visited and \
                    matrix[nextX][nextY] == string[index]:
                visited.add((nextX, nextY))
                if search(nextX, nextY, index + 1, visited):
                    return True
                visited.discard((nextX, nextY))
        return False

    if not matrix:
        return False
    if len(matrix[0]) * len(matrix) < len(string):
        return False
    positions = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == string[0]:
                positions.append((i, j))
    if positions and len(string) == 1:
        return True
    for position in positions:
        if search(position[0], position[1], 1, {position}):
            return True
    return False


def hasPathVersion2(matrix, string):
    def dfs(currentX, currentY, index):
        if not 0 <= currentX < len(matrix) or not 0 <= currentY < len(matrix[0]) or matrix[currentX][currentY] != string[index]:
            return False
        if index == len(string) - 1:
            return True
        temp = matrix[currentX][currentY]
        matrix[currentX][currentY] = '0'
        result = False
        for direction in directions:
            result |= dfs(currentX + direction[0], currentY + direction[1], index + 1)
        matrix[currentX][currentY] = temp
        return result

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if dfs(i, j, 0):
                return True
    return False


hasPath([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCEFSADEESE")
hasPath([["a", "a"]], "aaa")
hasPath([["A"],["A"],["C"]], "AAA")
hasPathVersion2([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
hasPathVersion2([['a']], 'a')
