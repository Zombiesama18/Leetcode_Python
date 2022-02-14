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
