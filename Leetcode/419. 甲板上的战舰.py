"""
419. 甲板上的战舰
给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。
战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，
其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。
"""
from typing import List


def countBattleships(board: List[List[str]]) -> int:
    result = 0
    row, col = len(board), len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'X':
                board[i][j] = '.'
                for k in range(i + 1, row):
                    if board[k][j] != 'X':
                        break
                    board[k][j] = '.'
                for k in range(j + 1, col):
                    if board[i][k] != 'X':
                        break
                    board[i][k] = '.'
                result += 1
    return result


