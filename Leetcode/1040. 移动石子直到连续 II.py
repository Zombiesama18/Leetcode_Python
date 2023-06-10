"""
1040. 移动石子直到连续 II

在一个长度 无限 的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作 端点石子 。
每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。
值得注意的是，如果石子像 stones = [1,2,5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），
该石子都仍然会是端点石子。
当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。
"""
from typing import List


def numMovesStonesII(stones: List[int]) -> List[int]:
    length = len(stones)
    stones.sort()
    max_result = stones[-1] - stones[0] + 1 - length - min(stones[-1] - stones[-2] - 1, stones[1] - stones[0] - 1)
    min_result = max_result
    right = 0
    for left in range(length):
        while right + 1 < length and stones[right + 1] - stones[left] < length:
            right += 1
        cost = length - (right - left + 1)
        if right - left + 1 == length - 1 and stones[right] - stones[left] + 1 == length - 1:
            cost = 2
        min_result = min(min_result, cost)
    return [min_result, max_result]


numMovesStonesII([7, 4, 9])
numMovesStonesII([6,5,4,3,10])


