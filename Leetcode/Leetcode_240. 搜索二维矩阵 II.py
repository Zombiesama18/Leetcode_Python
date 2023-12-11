# 240. 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
def searchMatrix(matrix: [[int]], target: int) -> bool:
    row, col = len(matrix), len(matrix[0])
    currentRow, currentCol = 0, col - 1
    while currentRow < row and currentCol >= 0:
        if matrix[currentRow][currentCol] == target:
            return True
        if matrix[currentRow][currentCol] > target:
            currentCol -= 1
        else:
            currentRow += 1
    return False


searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
