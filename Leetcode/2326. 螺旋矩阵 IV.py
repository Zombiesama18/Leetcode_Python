"""
2326. 螺旋矩阵 IV
给你两个整数：m 和 n ，表示矩阵的维数。
另给你一个整数链表的头节点 head 。
请你生成一个大小为 m x n 的螺旋矩阵，矩阵包含链表中的所有整数。
链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。如果还存在剩余的空格，则用 -1 填充。
返回生成的矩阵。
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    result = [[-1 for _ in range(n)] for _ in range(m)]
    index_x, index_y = 0, 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0
    while head:
        result[index_x][index_y] = head.val
        head = head.next
        next_x, next_y = index_x + directions[direction % 4][0], index_y + directions[direction % 4][1]
        if not 0 <= next_x < m or not 0 <= next_y < n or result[next_x][next_y] != -1:
            direction += 1
            next_x, next_y = index_x + directions[direction % 4][0], index_y + directions[direction % 4][1]
        index_x = next_x
        index_y = next_y
    return result


def spiralMatrix_v2(m: int, n: int, head: List[int]) -> List[List[int]]:
    result = [[-1 for _ in range(n)] for _ in range(m)]
    index_x, index_y = 0, 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0
    for i in range(len(head)):
        result[index_x][index_y] = head[i]
        next_x, next_y = index_x + directions[direction % 4][0], index_y + directions[direction % 4][1]
        if not 0 <= next_x < m or not 0 <= next_y < n or result[next_x][next_y] != -1:
            direction += 1
            next_x, next_y = index_x + directions[direction % 4][0], index_y + directions[direction % 4][1]
        index_x = next_x
        index_y = next_y
    return result


spiralMatrix_v2(m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0])
