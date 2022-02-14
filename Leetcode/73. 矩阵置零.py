# 73. 矩阵置零
# 给定一个 m x n1 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
def setZeroes_selfmade(matrix):
    zeroRow = set()
    zeroCol = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroRow.add(i)
                zeroCol.add(j)
    for i in zeroRow:
        for j in range(cols):
            matrix[i][j] = 0
    for j in zeroCol:
        for i in range(rows):
            matrix[i][j] = 0
    return matrix


matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
setZeroes_selfmade(matrix2)


def setZeroes_optimized(matrix):
    rows, cols = len(matrix), len(matrix[0])
    flag_row0 = any(matrix[0][i] == 0 for i in range(cols))
    flag_col0 = any(matrix[i][0] == 0 for i in range(rows))
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if flag_row0:
        for i in range(cols):
            matrix[0][i] = 0
    if flag_col0:
        for i in range(rows):
            matrix[i][0] = 0
    return matrix


setZeroes_optimized(matrix1)
