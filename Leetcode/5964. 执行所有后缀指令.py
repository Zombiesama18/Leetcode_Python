"""
5964. 执行所有后缀指令
现有一个 n x n 大小的网格，左上角单元格坐标 (0, 0) ，右下角单元格坐标 (n - 1, n - 1) 。给你整数 n 和一个整数数组 startPos ，
其中 startPos = [startrow, startcol] 表示机器人最开始在坐标为 (startrow, startcol) 的单元格上。
另给你一个长度为 m 、下标从 0 开始的字符串 s ，其中 s[i] 是对机器人的第 i 条指令：
'L'（向左移动），'R'（向右移动），'U'（向上移动）和 'D'（向下移动）。
机器人可以从 s 中的任一第 i 条指令开始执行。它将会逐条执行指令直到 s 的末尾，但在满足下述条件之一时，机器人将会停止：
下一条指令将会导致机器人移动到网格外。
没有指令可以执行。
返回一个长度为 m 的数组 answer ，其中 answer[i] 是机器人从第 i  条指令 开始  ，可以执行的 指令数目 。
"""
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directionDict = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
        result = []
        for i in range(len(s)):
            counter = 0
            currentPosition = startPos
            for j in range(i, len(s)):
                if 0 <= currentPosition[0] + directionDict[s[j]][0] < n and \
                        0 <= currentPosition[1] + directionDict[s[j]][1] < n:
                    currentPosition = [currentPosition[0] + directionDict[s[j]][0],
                                       currentPosition[1] + directionDict[s[j]][1]]
                    counter += 1
                else:
                    break
            result.append(counter)
        return result




