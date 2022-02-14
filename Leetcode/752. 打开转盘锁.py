# 752. 打开转盘锁（BFS，需要复习）
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
from collections import deque, Generator


def openLock(deadends: [str], target: str) -> int:
    def charPrev(num: str) -> str:
        return '9' if num == '0' else str(int(num) - 1)

    def charSucc(num: str) -> str:
        return '0' if num == '9' else str(int(num) + 1)

    def getNext(status: str):
        charList = list(status)
        for i in range(4):
            currentChar = charList[i]
            charList[i] = charPrev(currentChar)
            yield ''.join(charList)
            charList[i] = charSucc(currentChar)
            yield ''.join(charList)
            charList[i] = currentChar

    if target == '0000':
        return 0
    deadends = set(deadends)
    if '0000' in deadends:
        return -1
    q = deque([('0000', 0)])
    traversedCombination = {'0000'}
    while q:
        currentStatus, step = q.popleft()
        for nextStatus in getNext(currentStatus):
            if nextStatus not in traversedCombination and nextStatus not in deadends:
                if nextStatus == target:
                    return step + 1
                q.append((nextStatus, step + 1))
                traversedCombination.add(nextStatus)
    return -1


openLock(["0201","0101","0102","1212","2002"], "0202")
