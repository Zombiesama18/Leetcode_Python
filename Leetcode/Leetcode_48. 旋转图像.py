# 48. 旋转图像
# 给定一个 n1×n1 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


def rotate(matrix):
    length = len(matrix[0])
    for i in range(int((length + 1) / 2) + 1):
        for j in range(i, length - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[length - 1 - j][i]
            matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
            matrix[j][length - 1 - i] = temp
    return matrix


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
rotate(matrix)
