"""
1033. 移动石子直到连续

三枚石子放置在数轴上，位置分别为 a，b，c。
每一回合，你可以从两端之一拿起一枚石子（位置最大或最小），并将其放入两端之间的任一空闲位置。形式上，
假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。那么就可以从位置 x 或者是位置 z 拿起一枚石子，
并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
"""
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = list(sorted([a, b, c]))
        result1, result2 = 0, 0
        if b - a > 1:
            result1 += 1
        if c - b > 1:
            result1 += 1
        if b - a == 2 or c - b == 2:
            result1 = 1
        result2 += c - a - 2
        return [result1, result2]


Solution().numMovesStones(3, 5, 1)
