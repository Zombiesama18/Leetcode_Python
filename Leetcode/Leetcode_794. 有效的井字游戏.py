"""
794. 有效的井字游戏
给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。
以下是井字游戏的规则：
玩家轮流将字符放入空位（' '）中。
玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。
"""
import collections


def validTicTacToe(board: [str]) -> bool:
    x_counter, o_counter = sum(element == 'X' for row in board for element in row), \
                           sum(element == 'O' for row in board for element in row)
    if o_counter > x_counter or x_counter > o_counter + 1:
        return False

    def is_valid(target):
        return any(board[i][:] == target * 3 or board[0][i] == board[1][i] == board[2][i] == target for i in range(3)) \
               or board[0][0] == board[1][1] == board[2][2] == target \
               or board[0][2] == board[1][1] == board[2][0] == target

    if x_counter == o_counter:
        return not is_valid('X')
    return not is_valid('O')


validTicTacToe(["XO ","XO ","XO "])
validTicTacToe(["XXX","OOX","OOX"])
