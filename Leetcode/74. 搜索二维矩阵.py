# 74. 搜索二维矩阵
# 编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
import bisect


def searchMatrix(matrix: [[int]], target: int):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    targetRow = 0
    for i in range(rows):
        targetRow = i
        if target < matrix[i][-1]:
            break
        if target == matrix[i][-1]:
            return True
    for j in range(cols):
        if matrix[targetRow][j] == target:
            return True
    return False


matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 3
searchMatrix(matrix1, target1)
matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target2 = 13
searchMatrix(matrix2, target2)
searchMatrix(matrix1, target1)


def searchMatrixBinarySearch(matrix: [[int]], target: int):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])

    def binarySearchFirstColumn(target):
        low = -1
        high = rows - 1
        while low < high:
            mid = int((low + high + 1) / 2)
            if target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid
        return low

    def binarySearchRow(series, target):
        low = -1
        high = cols - 1
        while low < high:
            mid = int((low + high + 1) / 2)
            if target == series[mid]:
                return True
            elif target < series[mid]:
                high = mid - 1
            else:
                low = mid
        return False

    targetRow = binarySearchFirstColumn(target)
    return binarySearchRow(matrix[targetRow], target)


searchMatrixBinarySearch(matrix1, target1)
searchMatrixBinarySearch(matrix2, target2)
searchMatrixBinarySearch([[1]], 0)


def searchMatrixBuiltinBisect(matrix: [[int]], target: int):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    firstColumn = []
    for i in range(rows):
        firstColumn.append(matrix[i][0])
    targetRow = bisect.bisect_right(firstColumn, target)
    targetRow = targetRow - 1 if targetRow > 0 else targetRow
    targetCol = bisect.bisect_left(matrix[targetRow], target)
    targetCol = cols - 1 if targetCol == cols else targetCol
    return matrix[targetRow][targetCol] == target


searchMatrixBuiltinBisect(matrix1, target1)
searchMatrixBuiltinBisect(matrix2, target2)
searchMatrixBuiltinBisect([[1]], target2)
