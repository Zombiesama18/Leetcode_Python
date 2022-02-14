# 54. 螺旋矩阵
# 给你一个 m 行 n1 列的矩阵 matrix2 ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
def spiralOrder_selfmade(matrix):
    if not matrix:
        return None
    if len(matrix) == 1:
        return matrix[0]
    result = list()
    if len(matrix[0]) == 1:
        for i in range(len(matrix)):
            result.append(matrix[i][0])
        return result
    rows = len(matrix[0])
    cols = len(matrix)
    layers = int((min(rows, cols) + 1) / 2)
    for layer in range(layers):
        for row in range(layer, rows - 1 - layer):
            result.append(matrix[layer][row])
        for col in range(layer, cols - 1 - layer):
            result.append(matrix[col][rows - 1 - layer])
        for row in range(rows - 1 - layer, layer, -1):
            if matrix[cols - 1 - layer][row] not in result:
                result.append(matrix[cols - 1 - layer][row])
        for col in range(cols - 1 - layer, layer, -1):
            if matrix[col][layer] not in result:
                result.append(matrix[col][layer])
        if layer > 0 and layer == rows - 1 - layer and layer == cols - 1 - layer:
            result.append(matrix[layer][layer])
    return result


matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spiralOrder_selfmade(matrix2)
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
result = spiralOrder_selfmade(matrix2)
matrix2 = [[3], [2]]
spiralOrder_selfmade(matrix2)
matrix2 = [[6, 9, 7]]
spiralOrder_selfmade(matrix2)
matrix2 = [[7], [9], [6]]
spiralOrder_selfmade(matrix2)
matrix2 = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
spiralOrder_selfmade(matrix2)


def spiralOrder_recommended(matrix):
    if not matrix or not matrix[0]:
        return list()
    rows = len(matrix)
    cols = len(matrix[0])
    result = list()
    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        for row in range(top + 1, bottom + 1):
            result.append(matrix[row][right])
        if left < right and top < bottom:
            for col in range(right - 1, left, - 1):
                result.append(matrix[bottom][col])
            for row in range(bottom, top, -1):
                result.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return result
