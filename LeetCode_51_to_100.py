import bisect
import datetime
import itertools

import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 工具方法
def generateListNode(nodeValues: list):
    l1 = ListNode(nodeValues.pop(0))
    head = l1
    while nodeValues:
        head.next = ListNode(nodeValues.pop(0))
        head = head.next
    return l1


def traverseListNode(head):
    while head:
        print(head.val, end='->')
        head = head.next


# 53. 最大子序和
# 给定一个整数数组 nums1 ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


def maxSubArray(nums):
    subsets = []

    def get_cont_subsets():
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subsets.append(nums[i: j])

    get_cont_subsets()
    sums = []
    for i in subsets:
        sums.append(sum(i))
    return max(sums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray(nums)


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


# 55. 跳跃游戏
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。


# 就是看序号加数值能不能大于终点
def canJump(nums):
    dest = nums[-1]
    for i, v in enumerate(nums[0:-1]):
        if i + v >= dest:
            return True
    return False


nums = [3, 2, 1, 0, 4]
canJump(nums)


# 56. 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。


def merge(intervals):
    output = []
    result = []
    intervals.sort()
    for i in range(0, (len(intervals)) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            output.append([intervals[i][0], intervals[i + 1][1]])
        else:
            output.append(intervals[i])
    output.append(intervals[-1])
    result.append(output[0])
    for i in range(1, len(output)):
        if not (output[i][0] >= output[i - 1][0] and output[i][1] <= output[i - 1][1]):
            result.append(output[i])
    return result


intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
merge(intervals)


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


# 61. 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
def rotateRight(head: ListNode, k: int):
    if not head or k == 0:
        return head
    nodeStack = list()
    while head:
        nodeStack.append(head)
        head = head.next
    index = k % len(nodeStack)
    head = nodeStack[-index]
    nodeStack[-1].next = nodeStack[0]
    nodeStack[-index - 1].next = None
    return head


head1 = generateListNode([1, 2, 3, 4, 5])
traverseListNode(head1)
head1 = rotateRight(head1, 2)
traverseListNode(head1)
head2 = generateListNode([0, 1, 2])
traverseListNode(head2)
head2 = rotateRight(head2, 4)
traverseListNode(head2)
head3 = generateListNode([1])
traverseListNode(head3)
head3 = rotateRight(head3, 1)
traverseListNode(head3)


# 62. 不同路径
# 一个机器人位于一个 m x n1 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？


def uniquePaths(m, n):
    finish = [n, m]

    def recursion(now, direction):
        global counter
        temp = [now[0] + direction[0], now[1] + direction[1]]
        if temp == finish:
            counter += 1
            return
        if temp[0] < finish[0]:
            recursion(temp, [1, 0])
        if temp[1] < finish[1]:
            recursion(temp, [0, 1])

    recursion([1, 1], [1, 0])
    recursion([1, 1], [0, 1])
    return


counter = 0
m = 7
n = 3
uniquePaths(m, n)
print(counter)


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


# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n1 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n1 是一个正整数。


def climbStairs(n):
    def recursion(now, step):
        temp = now + step
        if now + step == n:
            global counter
            counter += 1
            return
        if temp + 2 <= n:
            recursion(temp, 2)
        if temp + 1 <= n:
            recursion(temp, 1)

    if n > 0:
        recursion(0, 1)
    if n > 1:
        recursion(0, 2)
    return


counter = 0
climbStairs(4)
print(counter)


# 72. 编辑距离（需要复习）
# 给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符


# 使用动态规划（Dynamic Planining)，dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
# 当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；等于左上角的值，相当于直接把前一个照搬过来。
# 当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，等于上、左上和左的最小值再加一，相当于在之前操作的基础上进行了一步操作。
# 其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    # 初始化
    for i in range(1, len(word1) + 1):
        dp[i][0] = dp[i - 1][0] + 1
    for j in range(1, len(word2) + 1):
        dp[0][j] = dp[0][j - 1] + 1
    # 进入循环
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:  # dp中的序号比word数组中序号多1
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    print(dp)
    return dp[-1][-1]


word1 = "intention"
word2 = "execution"
minDistance(word1, word2)


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


# 74. 搜索二维矩阵
# 编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
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
# 75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。


def sortColors(nums):
    output = []
    index_white = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            output.insert(0, 0)
            index_white = index_white + 1
        elif nums[i] == 1:
            output.insert(index_white, 1)
        elif nums[i] == 2:
            output.insert(-1, 2)
        else:
            print('出现了其他颜色，不计入统计')
    print(output)


sortColors([2, 0, 2, 1, 1, 0])


# 76. 最小覆盖子串（需要复习）
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n1) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。


# 使用滑动窗口思想，用i,j表示滑动窗口的左边界和右边界，通过改变i,j来扩展和收缩滑动窗口，可以想象成一个窗口在字符串上游走，当这个窗口包含的元素满足条件，即包含字符串T的所有元素，记录下这个滑动窗口的长度j-i+1，这些长度中的最小值就是要求的结果
def minWindow(s, t):
    subsets = []
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            temp = s[i:j]
            if set(t).issubset(set(temp)):
                subsets.append(temp[:])
    length = []
    for i in subsets:
        length.append(len(i))
    return subsets[length.index(min(length))]


s = "ADOBECODEBANC"
t = "ABC"
minWindow(s, t)


# 78. 子集
# 给定一组不含重复元素的整数数组 nums1，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。


def subsets(nums):
    output = []

    def recursion(start, comb):
        output.append(comb[:])
        for i in range(start, len(nums)):
            recursion(i + 1, comb + [nums[i]])

    recursion(0, [])
    return output


nums = [1, 2, 3]
subsets(nums)


# 79. 单词搜索（需要复习）
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 这个方法有缺陷
# def exist(board, word):
#     maxx = len(board)
#     maxy = len(board[0])
#     positions = []
#     true_false = []
#
#     def letter_is_around(posits1, posits2):
#         if type(posits1[0]) is list:
#             for po1 in posits1:
#                 for po2 in posits2:
#                     if is_around(po1, po2):
#                         return po2
#         if type(posits1[0]) is int:
#             po1 = posits1
#             for po2 in posits2:
#                 if is_around(po1, po2):
#                     return po2
#         return False
#
#     def is_around(posit1, posit2):
#         if posit1[1] == posit2[1] and (posit1[0] == posit2[0] + 1 or posit1[0] == posit2[0] - 1):
#             return True
#         if posit1[0] == posit2[0] and (posit1[1] == posit2[1] + 1 or posit1[1] == posit2[1] - 1):
#             return True
#         return False
#
#     for i in range(len(word)):
#         positions.append([])
#         for j in range(maxx):
#             for k in range(maxy):
#                 if board[j][k] == word[i]:
#                     positions[i].append([j, k])
#     temp = letter_is_around(positions[0], positions[1])
#     if type(temp) is list:
#         true_false.append(True)
#     if temp is False:
#         return False
#     for i in range(2, len(positions)):
#         temp = letter_is_around(temp, positions[i])
#         if type(temp) is list:
#             true_false.append(True)
#         if temp is False:
#             return False
#     return min(true_false)


# 找到起始字母后向四个方向寻找，使用矩阵来表示访问过
def exist(board, word):
    maxx = len(board)
    maxy = len(board[0])
    visited = [[False] * maxy for _ in range(maxx)]
    move_rows = [-1, 1, 0, 0]
    move_cols = [0, 0, 1, -1]

    inital_position = []
    for i in range(maxx):
        for j in range(maxy):
            if board[i][j] == word[0]:
                inital_position.append([i, j])

    def recursion(now, counter):
        if board[now[0]][now[1]] != word[counter]:
            return False
        if counter == len(word) - 1:
            return True
        visited[now[0]][now[1]] = True
        for i in range(4):
            next_x = now[0] + move_rows[i]
            next_y = now[1] + move_cols[i]
            if 0 <= next_x < maxx and 0 <= next_y < maxy and not visited[next_x][next_y] and recursion([next_x, next_y],
                                                                                                       counter + 1):
                return True
        visited[now[0]][now[1]] = False
        return False

    for i in range(len(inital_position)):
        if recursion(inital_position[i], 0):
            return True
    return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = 'ABCB'
exist(board, word)


# 80. 删除有序数组中的重复项 II
# 给你一个有序数组 nums1 ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
def removeDuplicates(nums: [int]) -> int:
    counterForThisDigit = 1
    index = 1
    while index < len(nums):
        if nums[index] == nums[index - 1]:
            if counterForThisDigit == 2:
                nums.pop(index)
            else:
                counterForThisDigit += 1
                index += 1
        else:
            counterForThisDigit = 1
            index += 1
    return index


nums1 = [1, 1, 1, 2, 2, 3]
removeDuplicates(nums1)
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
removeDuplicates(nums2)


# 81. 搜索旋转排序数组 II
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n1-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。
# 如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
def searchBinarySearch(nums: [int], target: int) -> bool:
    if not nums:
        return False
    length = len(nums)
    if length == 1:
        return target == nums[0]
    left, right = 0, length - 1
    while left <= right:
        mid = left + right >> 1
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] and nums[right] == nums[mid]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


# 82. 删除排序链表中的重复元素 II
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。
# 返回同样按升序排列的结果链表。
def deleteDuplicatesII(head: ListNode):
    if not head:
        return head
    sentinel = ListNode(0, head)
    isDuplicate = False
    formerNode = sentinel
    currentNode = head
    while currentNode.next:
        if currentNode.val == currentNode.next.val:
            currentNode = currentNode.next
            isDuplicate = True
        else:
            if isDuplicate:
                isDuplicate = False
            else:
                formerNode.next = currentNode
                formerNode = currentNode
            currentNode = currentNode.next
    if isDuplicate:
        formerNode.next = None
    else:
        formerNode.next = currentNode
    return sentinel.next


head1 = generateListNode([1, 1, 1, 2, 3])
traverseListNode(head1)
head1 = deleteDuplicatesII(head1)
traverseListNode(head1)
head2 = generateListNode([1, 2, 3, 3, 4, 4, 5])
traverseListNode(head2)
head2 = deleteDuplicatesII(head2)
traverseListNode(head2)


# 83. 删除排序链表中的重复元素
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
# 返回同样按升序排列的结果链表。
def deleteDuplicatesI(head: ListNode):
    if not head:
        return head
    formerNode = head
    currentNode = head.next
    while currentNode:
        if currentNode.val == formerNode.val:
            currentNode = currentNode.next
        else:
            formerNode.next = currentNode
            formerNode = currentNode
            currentNode = currentNode.next
    formerNode.next = None
    return head


head1 = generateListNode([1, 1, 2])
traverseListNode(head1)
head1 = deleteDuplicatesI(head1)
traverseListNode(head1)
head2 = generateListNode([1, 1, 2, 3, 3])
traverseListNode(head2)
head2 = deleteDuplicatesI(head2)
traverseListNode(head2)


# 84. 柱状图中最大的矩形
# 给定 n1 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


def largestRectangleArea(heights):
    areas = heights[:]
    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            areas.append(min(heights[i: j + 1]) * (j - i + 1))
    return max(areas)


heights = [2, 1, 5, 6, 2, 3]
largestRectangleArea(heights)


# 88. 合并两个有序数组
# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
# 初始化nums1 和 nums2 的元素数量分别为m 和 n1 。你可以假设nums1 的空间大小等于m + n1，这样它就有足够的空间保存来自 nums2 的元素。
def merge(nums1: [int], m: int, nums2: [int], n: int):
    temp = nums1[0:m]
    counter = 0
    while temp or nums2:
        numFromOne = temp[0] if temp else float('INF')
        numFromTwo = nums2[0] if nums2 else float('INF')
        if numFromTwo > numFromOne:
            nums1[counter] = numFromOne
            temp.pop(0)
        else:
            nums1[counter] = numFromTwo
            nums2.pop(0)
        counter += 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)


# 90. 子集 II（需要复习）
# 给你一个整数数组 nums1 ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
def subsetsWithDupEnumerate(nums: [int]):
    if not nums:
        return [[]]
    result = list()
    length = len(nums)
    nums = sorted(nums)

    def subsetsHelper(subset, counter):
        if subset not in result:
            result.append(subset)
        for i in range(counter, length):
            subsetsHelper(subset + [nums[i]], i + 1)
        return

    subsetsHelper([], 0)
    return result


nums = []
digitNumber = 16
for _ in range(digitNumber):
    nums.append(np.random.randint(0, digitNumber))
startTime = datetime.datetime.now()
# nums1 = [1,2,2]
result1 = subsetsWithDupEnumerate(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)


def subsetsWithDupbyHashCode(nums: [int]):
    if not nums:
        return [[]]
    result = {}
    length = len(nums)
    nums = sorted(nums)

    def subsetsHelper(subset, counter):
        hashCode = hash(tuple(subset))
        if hashCode not in result:
            result[hashCode] = subset
        for i in range(counter, length):
            subsetsHelper(subset + [nums[i]], i + 1)
        return

    subsetsHelper([], 0)
    return list(result.values())


nums = []
digitNumber = 10
for _ in range(digitNumber):
    nums.append(np.random.randint(0, digitNumber))
startTime = datetime.datetime.now()
result2 = subsetsWithDupbyHashCode(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)


def subsetsWithDupbySet(nums: [int]):
    result = []
    length = len(nums)
    nums = sorted(nums)
    temp = set()

    def subsetsHelper(subset, counter):
        temp.add(tuple(subset))
        for i in range(counter, length):
            subsetsHelper(subset + [nums[i]], i + 1)
        return

    subsetsHelper([], 0)
    result.extend(temp)
    return result


result4 = subsetsWithDupbySet(nums)


def subsetsWithDupbyBuiltinFunction(nums: [int]):
    result = [[]]
    nums.sort()
    for i in range(1, len(nums) + 1):
        result.extend(set(itertools.combinations(nums, i)))
    return result


startTime = datetime.datetime.now()
result3 = subsetsWithDupbyBuiltinFunction(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)


def subsetsWithDupbyLogicMethod(nums: [int]):
    temp = list()
    result = list()
    length = len(nums)

    def dfsHelper(choosePre, currentIndex):
        if currentIndex == length:
            result.append(temp)
        dfsHelper(False, currentIndex + 1)
        if not choosePre and nums[currentIndex - 1] == nums[currentIndex]:
            return
        temp.append(nums[currentIndex])
        dfsHelper(True, currentIndex + 1)
        temp.pop(-1)

    nums.sort()
    dfsHelper(False, 0)
    return result
# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历（左，根，右）。


def inorderTraversal(root):
    values = []

    def recursion(node):
        if node.left:
            recursion(node.left)
        values.append(node.val)
        if node.right:
            recursion(node.right)

    recursion(root)
    return values


l3 = TreeNode(3)
l2 = TreeNode(2)
l1 = TreeNode(1)
l1.right = l2
l2.left = l3
inorderTraversal(l1)


# 92. 反转链表 II
# 反转从位置 m 到 n1 的链表。请使用一趟扫描完成反转。
def reverseBetween(head: ListNode, left: int, right: int):
    if left < 1 or right <= left or not head:
        return head
    i = 0
    sentinel = ListNode(0)
    sentinel.next = head
    node = sentinel
    stack = list()
    while i < left - 1:
        node = node.next
        i += 1
    leftStart = node
    while i < right:
        node = node.next
        stack.append(node)
        i += 1
    rightEnd = node.next
    while stack:
        leftStart.next = stack.pop()
        leftStart = leftStart.next
    leftStart.next = rightEnd
    return sentinel.next


# 工具方法
def generateListNode(nodeValues: list):
    l1 = ListNode(nodeValues.pop(0))
    head = l1
    while nodeValues:
        head.next = ListNode(nodeValues.pop(0))
        head = head.next
    return l1


def traverseListNode(head):
    while head:
        print(head.val, end='->')
        head = head.next


head = generateListNode([1, 2, 3, 4, 5])
reverseBetween(head, 2, 4)
traverseListNode(head)


# 96. 不同的二叉搜索树（需要复习）
# 给定一个整数 n1，求以 1 ... n1 为节点组成的二叉搜索树有多少种？
# 假设f(n1)为整数n的二叉搜索树数，而对于一个大于n的数m，有f(m)=f(n1)f(m-n1-1)，即左边是n个元素的二叉搜索树，右边是m-n1-1个元素的二叉搜索树。
# 已知f(0)=1，f(1)=1，对于f(3)，有f(3)=f(0)f(2)+f(1)f(1)+f(2)f(0)，对于每个大于2的整数n都可以细分


def numTrees(n):
    store = [1, 1]
    if n < 2:
        return store[n]
    for m in range(2, n + 1):  # 从2一步一步计算到n
        counter = 0
        for i in range(m):
            counter += store[i] * store[m - 1 - i]
        store.append(counter)
    return store[n]


n = 3
numTrees(n)


# 98. 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
def isValidBST(root):
    if root.left:
        if root.left.val > root.val:
            return False
        else:
            isValidBST(root.left)
    if root.right:
        if root.right.val < root.val:
            return False
        else:
            isValidBST(root.right)
    return True


l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(6)
l5.left = l1
l5.right = l4
l4.left = l3
l4.right = l6
isValidBST(l5)
l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l2.left = l1
l2.right = l3
isValidBST(l2)
