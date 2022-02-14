import datetime
import random
import string


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateListNode(nodeValues: list):
    l1 = ListNode(nodeValues.pop(0))
    head = l1
    while nodeValues:
        head.next = ListNode(nodeValues.pop(0))
        head = head.next
    return l1


def traverseListNode(head):
    while head:
        print(head.val, end='->')
        head = head.next


# 705. 设计哈希集合
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 实现 MyHashSet 类：
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
class MyHashSet:
    def __init__(self):
        self.dict = {}
        self.base = 13

    def add(self, key: int):
        hashcode = key % self.base
        if not self.dict.get(hashcode):
            self.dict[hashcode] = [key]
        else:
            if key not in self.dict[hashcode]:
                self.dict[hashcode].append(key)
        return

    def remove(self, key: int):
        hashcode = key % self.base
        if hashcode in self.dict.keys():
            if key in self.dict[hashcode]:
                if len(self.dict[hashcode]) == 1:
                    self.dict.pop(hashcode)
                else:
                    self.dict[hashcode].remove(key)
        return

    def contains(self, key: int):
        hashcode = key % self.base
        if hashcode in self.dict.keys():
            if key in self.dict[hashcode]:
                return True
        return False


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.contains(1)
myHashSet.contains(3)
myHashSet.add(2)
myHashSet.contains(2)
myHashSet.remove(2)
myHashSet.contains(2)


# 706. 设计哈希映射
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 13
        self.map = [None for _ in range(self.base)]
        self.keys = list()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = key % self.base
        if self.map[hashcode] is None:
            self.map[hashcode] = [Entry(key, value)]
            self.keys.append(key)
        elif key in self.keys:
            for subEntry in self.map[hashcode]:
                if subEntry.key == key:
                    subEntry.value = value
        else:
            self.map[hashcode].append(Entry(key, value))
            self.keys.append(key)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = key % self.base
        if self.map[hashcode]:
            for subEntry in self.map[hashcode]:
                if subEntry.key == key:
                    return subEntry.value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            hashcode = key % self.base
            for subEntry in self.map[hashcode]:
                if subEntry.key == key:
                    self.map[hashcode].remove(subEntry)
            self.keys.remove(key)


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
myHashMap.get(1)
myHashMap.get(3)
myHashMap.put(2, 1)
myHashMap.get(2)
myHashMap.remove(2)
myHashMap.get(2)


# 783. 二叉搜索树节点最小距离
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 结果：竖直方法不如展开方法
def minDiffInBSTByFlatting(root: TreeNode) -> int:
    traversal = []

    def subInorderTraversal(node):
        if not node:
            return
        subInorderTraversal(node.left)
        traversal.append(node.val)
        subInorderTraversal(node.right)
        return

    subInorderTraversal(root)
    minDistance = float('INF')
    for i in range(len(traversal) - 1):
        if abs(traversal[i + 1] - traversal[i]) < minDistance:
            minDistance = abs(traversal[i + 1] - traversal[i])
    return minDistance


# 1002. 查找常用字符
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。


def commonChars(A):
    def recursion(comb, ind):
        if ind == len(A):
            return comb
        temp = []
        A[ind] = list(A[ind])
        for i in range(len(comb)):
            for j in range(len(A[ind])):
                if comb[i] == A[ind][j]:
                    temp.append(comb[i])
                    A[ind].remove(comb[i])
                    break
        return recursion(temp, ind + 1)

    return recursion(A[0], 1)


A = ["bella", "label", "roller"]
commonChars(A)


# 1006. 笨阶乘
# 通常，正整数 n1 的阶乘是所有小于或等于 n1 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
# 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
# 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：
# 我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
# 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
# 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
def clumsy(N: int):
    operator = ['*', '/', '+', '-']
    operatorCounter = 0
    numStack = [N]
    numCounter = N - 1
    firstSet = True

    def operate(currentOperator):
        if currentOperator == '*':
            operateLatterNum = numStack.pop(-1)
            numStack.append(operateLatterNum * numStack.pop(-1))
        elif currentOperator == '/':
            operateLatterNum = numStack.pop(-1)
            numStack.append(int(numStack.pop(-1) / operateLatterNum))
        elif currentOperator == '+':
            if firstSet:
                operateLatterNum = numStack.pop(-1)
                numStack.append(numStack.pop(-1) + operateLatterNum)
            else:
                operateLatterNum = numStack.pop(-1)
                numStack.append(numStack.pop(-1) - operateLatterNum)
        else:
            operateLatterNum = numStack.pop(-1)
            numStack.append(numStack.pop(-1) - operateLatterNum)

    while numCounter > 0:
        currentOperator = operator[operatorCounter % 4]
        operatorCounter += 1
        numStack.append(numCounter)
        numCounter -= 1
        if currentOperator != '-':
            operate(currentOperator)
        else:
            firstSet = False
    for i in range(len(numStack)):
        if i != 0:
            numStack[i] = -numStack[i]
    return sum(numStack)


clumsy(4)


def clumsyVersion2(N: int):
    firstSet = True
    setNumber = N >> 2
    remainder = N % 4
    finalSetIfFirstSet = [0, 1, 2 * 1, int(3 * 2 / 1)]
    finalSetIfNotFirstSet = [0, - 1, - 2 * 1, -int(3 * 2 / 1)]
    result = []
    for i in range(setNumber):
        if firstSet:
            firstSet = False
            result.append(int(N * (N - 1) / (N - 2)) + N - 3)
        else:
            result.append(-int(N * (N - 1) / (N - 2)) + N - 3)
        N -= 4
    if firstSet:
        result.append(finalSetIfFirstSet[remainder])
    else:
        result.append(finalSetIfNotFirstSet[remainder])
    return sum(result)


# 1047. 删除字符串中的所有相邻重复项
# 给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
def removeDuplicates_first(s: str):
    if len(s) < 2:
        return s
    while True:
        changed = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                changed = True
                break
        if not changed:
            break
    return s


s = "abbaca"
removeDuplicates_first(s)


def removeDuplicates_second(s: str):
    if len(s) < 2:
        return s
    stack = list()
    for i in range(len(s)):
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    return ''.join(stack)


# s = "abbaca"
letters = string.ascii_letters[5:10]
s = ''
for i in range(50000):
    s += random.choice(letters)
start_time = datetime.datetime.now()
result1 = removeDuplicates_first(s)
end_time = datetime.datetime.now()
print(end_time - start_time)
start_time = datetime.datetime.now()
result2 = removeDuplicates_second(s)
end_time = datetime.datetime.now()
print(end_time - start_time)
print(result1 == result2)


# 1603. 设计停车系统
# 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
# 请你实现ParkingSystem类：
# ParkingSystem(int big, int medium, int small)初始化ParkingSystem类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType)检查是否有carType对应的停车位。carType有三种类型：大，中，小，分别用数字1，2和3表示。一辆车只能停在carType对应
# 尺寸的停车位中。如果没有空车位，请返回false，否则将该车停入车位并返回true。
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.maxNum = [big, medium, small]
        self.currentNum = [0, 0, 0]

    def addCar(self, carType: int):
        if carType < 1 or carType > 3:
            return False
        if self.currentNum[carType - 1] == self.maxNum[carType - 1]:
            return False
        else:
            self.currentNum[carType - 1] += 1
            return True


parkingSystem = ParkingSystem(1, 1, 0)
parkingSystem.addCar(1)
parkingSystem.addCar(2)
parkingSystem.addCar(3)
parkingSystem.addCar(1)


# 面试题 17.21. 直方图的水量（需要复习）
# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。感谢 Marcos 贡献此图。
# url: https://leetcode-cn.com/problems/volume-of-histogram-lcci/
def trap(height: [int]) -> int:
    length = len(height)
    highOfLastEdge = 0
    heightsFromLeft = [0 for _ in range(length)]
    heightsFromRight = [0 for _ in range(length)]
    result = 0
    for i in range(0, length):
        if height[i] > highOfLastEdge:
            highOfLastEdge = height[i]
        else:
            heightsFromLeft[i] = highOfLastEdge - height[i]
    highOfLastEdge = 0
    for i in range(length - 1, -1, -1):
        if height[i] > highOfLastEdge:
            highOfLastEdge = height[i]
        else:
            heightsFromRight[i] = highOfLastEdge - height[i]
    for i in range(length):
        result += min(heightsFromLeft[i], heightsFromRight[i])
    return result


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [5, 4, 1, 2]
height = [4, 2, 0, 3, 2, 5]
trap(height)
