# 59. 螺旋矩阵 II
# 给你一个正整数 n1 ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n1 x n1 正方形矩阵 matrix2 。
def generateMatrix(n: int):
    if n < 1:
        return []
    result = [[0] * n for _ in range(n)]
    left, right, top, bottom, number = 0, n - 1, 0, n - 1, 1
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result[top][col] = number
            number += 1
        for row in range(top + 1, bottom + 1):
            result[row][right] = number
            number += 1
        if left < right and top < bottom:
            for col in range(right - 1, left, -1):
                result[bottom][col] = number
                number += 1
            for row in range(bottom, top, -1):
                result[row][left] = number
                number += 1
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return result


# n1 = 1
# generateMatrix(n1)
n = 2
generateMatrix(n)
n = 3
generateMatrix(n)
