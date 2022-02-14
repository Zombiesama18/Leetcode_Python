# 488. 祖玛游戏
# 你正在参与祖玛游戏的一个变种。
# 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。
# 你的目标是 清空 桌面上所有的球。每一回合：
# 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
# 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
# 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
# 如果桌面上所有球都被移除，则认为你赢得本场游戏。
# 重复这个过程，直到你赢了游戏或者手中没有更多的球。
# 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，
# 计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。
import collections
import re
import itertools


def findMinStep(board: str, hand: str) -> int:
    def clean(s):
        # 消除桌面上需要消除的球
        n = 1
        while n:
            s, n = re.subn(r"(.)\1{2,}", "", s)
        return s

    hand = ''.join(sorted(hand))
    dq = collections.deque([(board, hand, 0)])
    visited = {(board, hand)}
    while dq:
        current_board, current_hand, current_step = dq.popleft()
        for i, j in itertools.product(range(len(current_board) + 1), range(len(current_hand))):
            # 当前球的颜色和上一个球的颜色相同
            if j > 0 and current_hand[j] == current_hand[j - 1]:
                continue
            # 只在连续相同颜色的球的开头位置
            if i > 0 and current_board[i - 1] == current_hand[j]:
                continue
            # 只在：当前球颜色与后面的球的颜色相同 和 当前后颜色相同且与当前颜色不同 放置球
            choose = False
            if 0 < i < len(current_board) and current_board[i - 1] == current_board[i]:
                choose = True
            if i < len(current_board) and current_board[i] == current_hand[j]:
                choose = True
            if choose:
                next_board = clean(current_board[:i] + current_hand[j] + current_board[i:])
                next_hand = current_hand[:j] + current_hand[j + 1:]
                if not next_board:
                    return current_step + 1
                if (next_board, next_hand) not in visited:
                    dq.append((next_board, next_hand, current_step + 1))
                    visited.add((next_board, next_hand))
    return -1



findMinStep("WRRBBW", "RB")
findMinStep("WWRRBBWW", "WRBRW")
