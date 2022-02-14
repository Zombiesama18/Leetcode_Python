# 1975. 最大方阵和
# 给你一个  n x n  的整数方阵  matrix  。你可以执行以下操作  任意次  ：
# 选择  matrix  中  相邻  两个元素，并将它们都 乘以  -1  。
# 如果两个元素有 公共边  ，那么它们就是 相邻  的。
# 你的目的是 最大化  方阵元素的和。请你在执行以上操作之后，返回方阵的  最大  和。
def maxMatrixSum(matrix: [[int]]) -> int:
    minusNumber = 0
    minMinusNumber = float('INF')
    result = 0
    row = len(matrix)
    for i in range(row):
        for j in range(row):
            minMinusNumber = min(abs(matrix[i][j]), minMinusNumber)
            if matrix[i][j] < 0:
                minusNumber += 1
            result += abs(matrix[i][j])
    return result - 2 * minMinusNumber if minusNumber % 2 != 0 else result


maxMatrixSum( [[1,-1],[-1,1]])
maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])



