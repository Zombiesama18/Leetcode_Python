# 773. 滑动谜题
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
import copy
from collections import deque


def slidingPuzzleByList(board: [[int]]) -> int:
    def getNext(status: [[int]]):
        position = getZeroPosition(status)
        statusCopy = copy.deepcopy(status)
        swapElement([1, position[1]], [0, position[1]], statusCopy)
        yield statusCopy
        if position[1] > 0:
            statusCopy = copy.deepcopy(status)
            swapElement([position[0], position[1] - 1], [position[0], position[1]], statusCopy)
            yield statusCopy
        if position[1] < 2:
            statusCopy = copy.deepcopy(status)
            swapElement([position[0], position[1]], [position[0], position[1] + 1], statusCopy)
            yield statusCopy

    def getZeroPosition(status: [[int]]):
        for i in range(2):
            for j in range(3):
                if status[i][j] == 0:
                    return [i, j]

    def swapElement(position1: [int], position2: [int], status: [[int]]):
        temp = status[position1[0]][position1[1]]
        status[position1[0]][position1[1]] = status[position2[0]][position2[1]]
        status[position2[0]][position2[1]] = temp

    target = [[1, 2, 3], [4, 5, 0]]
    if board == target:
        return 0
    traversedBoard = {(tuple(board[0]), tuple(board[1]))}
    q = deque([(board, 0)])
    while q:
        currentBoard, step = q.popleft()
        for nextStatus in getNext(currentBoard):
            if (tuple(nextStatus[0]), tuple(nextStatus[1])) not in traversedBoard:
                if nextStatus == target:
                    return step + 1
                q.append((nextStatus, step + 1))
                traversedBoard.add((tuple(nextStatus[0]), tuple(nextStatus[1])))
    return -1


slidingPuzzleByList([[1, 2, 3], [4, 0, 5]])
slidingPuzzleByList([[4, 1, 2], [5, 0, 3]])


def slidingPuzzleByString(board: [[int]]) -> int:
    target = [[1, 2, 3], [4, 5, 0]]
    if board == target:
        return 0
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    def getNext(status: str):
        status = list(status)
        currentPosition = status.index('0')
        for nextPosition in NEIGHBORS[currentPosition]:
            status[currentPosition], status[nextPosition] = status[nextPosition], status[currentPosition]
            yield ''.join(status)
            status[currentPosition], status[nextPosition] = status[nextPosition], status[currentPosition]

    initial = ''.join(str(num) for num in sum(board, []))
    target = ''.join(str(num) for num in sum(target, []))
    traversedCombination = {initial}
    q = deque([(initial, 0)])
    while q:
        currentStatus, step = q.popleft()
        for nextStatus in getNext(currentStatus):
            if nextStatus not in traversedCombination:
                if nextStatus == target:
                    return step + 1
                q.append((nextStatus, step + 1))
                traversedCombination.add(nextStatus)
    return -1




