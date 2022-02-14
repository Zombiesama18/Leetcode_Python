# 1958. 检查操作是否合法
# 给你一个下标从 0 开始的 8 x 8 网格 board ，其中 board[r][c] 表示游戏棋盘上的格子 (r, c) 。棋盘上空格用 '.' 表示，
# 白色格子用 'W' 表示，黑色格子用 'B' 表示。
# 游戏中每次操作步骤为：选择一个空格子，将它变成你正在执行的颜色（要么白色，要么黑色）。但是，合法 操作必须满足：
# 涂色后这个格子是 好线段的一个端点 （好线段可以是水平的，竖直的或者是对角线）。
# 好线段 指的是一个包含 三个或者更多格子（包含端点格子）的线段，线段两个端点格子为 同一种颜色 ，
# 且中间剩余格子的颜色都为 另一种颜色 （线段上不能有任何空格子）。你可以在下图找到好线段的例子：
# 给你两个整数 rMove 和 cMove 以及一个字符 color ，表示你正在执行操作的颜色（白或者黑），如果将格子 (rMove, cMove)
# 变成颜色 color 后，是一个 合法 操作，那么返回 true ，如果不是合法操作返回 false 。
def checkMove(board: [[str]], rMove: int, cMove: int, color: str) -> bool:
    def check(currentRow: int, currentCol: int, counter: int, direction: int, sourceColor: str):
        if board[currentRow][currentCol] == '.':
            return False
        if counter == 1 and board[currentRow][currentCol] == sourceColor:
            return False
        if board[currentRow][currentCol] == sourceColor:
            return True
        nextRow, nextCol = currentRow + directions[direction][0], currentCol + directions[direction][1]
        if 0 <= nextRow < row and 0 <= nextCol < col:
            return check(nextRow, nextCol, counter + 1, direction, sourceColor)
        return False

    row, col = 8, 8
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for i in range(len(directions)):
        nextRow, nextCol = rMove + directions[i][0], cMove + directions[i][1]
        if 0 <= nextRow < row and 0 <= nextCol < col and check(nextRow, nextCol, 1, i, color):
            return True
    return False


checkMove(board=[[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
                 [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
                 ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."],
                 [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], rMove=4, cMove=3,
          color="B")
checkMove(board=[[".", ".", ".", ".", ".", ".", ".", "."], [".", "B", ".", ".", "W", ".", ".", "."],
                 [".", ".", "W", ".", ".", ".", ".", "."], [".", ".", ".", "W", "B", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", "B", "W", ".", "."],
                 [".", ".", ".", ".", ".", ".", "W", "."], [".", ".", ".", ".", ".", ".", ".", "B"]], rMove=4, cMove=4,
          color="W")
