import datetime
import random
import string

from typing import List

from sortedcontainers import SortedList


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


# 406. 根据身高重建队列
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
def reconstructQueue(people):
    def get_higher_number(target, idx):
        counter = 0
        for i in range(idx):
            if target[0] < people[i][0] or target[0] == people[i][0]:
                counter += 1
        return counter

    while 1:
        unswap = True
        for i in range(len(people)):
            higher_persons = get_higher_number(people[i], i)
            if people[i][1] < higher_persons:
                temp = people[i - 1]
                people[i - 1] = people[i]
                people[i] = temp
                unswap = False
            if people[i][1] > higher_persons:
                temp = people[i + 1]
                people[i + 1] = people[i]
                people[i] = temp
                unswap = False
        if unswap:
            break
    return people


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
reconstructQueue(people)


# 416. 分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 注意:
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200


def canPartition(nums):
    subsets = []

    # 取所有子集
    def get_subsets(comb, start):
        subsets.append(comb)
        for i in range(start, len(nums)):
            get_subsets(comb + [nums[i]], i + 1)

    def is_equal(list1, list2):
        if sum(list1) == sum(list2):
            return True
        else:
            return False

    def get_comple(subset):
        if subset:
            # temp的分配在取subset中每个数字之前
            temp = nums.copy()
            for i in subset:
                temp.remove(i)
            return temp
        else:
            return nums

    get_subsets([], 0)
    total_list1 = []
    total_list2 = []
    for i in subsets:
        total_list1.append(i[:])
        complement = get_comple(i)
        total_list2.append(complement[:])
    for i in range(len(total_list1)):
        if is_equal(total_list1[i], total_list2[i]):
            return True
    return False


nums = [1, 5, 11, 5]
canPartition(nums)
nums = [1, 2, 3, 5]
canPartition(nums)


# 443. 压缩字符串
# 给定一组字符，使用原地算法将其压缩。
# 压缩后的长度必须始终小于或等于原数组长度。
# 数组的每个元素应该是长度为1的字符（不是 int 整数类型）。
# 在完成原地修改输入数组后，返回数组的新长度。
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
def compress(chars: List[str]):
    if len(chars) < 2:
        return len(chars)
    length = len(chars)
    wordCounter = 1
    modifyIndex = 0
    currentChar = chars[0]
    for i in range(0, length - 1):
        if currentChar == chars[i + 1]:
            if wordCounter == 1:
                modifyIndex += 1
            wordCounter += 1
            if wordCounter == 10:
                chars[modifyIndex] = '1'
                modifyIndex += 1
            if wordCounter > 10 and int(wordCounter / 10) != chars[modifyIndex - 1]:
                chars[modifyIndex - 1] = str(int(wordCounter / 10))
            chars[modifyIndex] = str(wordCounter % 10)
        else:
            currentChar = chars[i + 1]
            modifyIndex += 1
            wordCounter = 1
            chars[modifyIndex] = chars[i + 1]
    while len(chars) != modifyIndex + 1:
        chars.pop()
    return len(chars)


chars1 = ["a","a","b","b","c","c","c"]
compress(chars1)
chars2 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
compress(chars2)
chars3 = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
compress(chars3)
# 456. 132模式（加急）（需要复习）
# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列ai, aj, ak被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，
# 当给定有n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
# 注意：n1 的值小于15000。
def find132pattern_selfmade(nums):
    if len(nums) < 3:
        return False
    length = len(nums)
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            if nums[j] > nums[i]:
                for k in range(j + 1, length):
                    if nums[j] > nums[k] > nums[i]:
                        return True
    return False


nums1 = [1, 2, 3, 4]
find132pattern_selfmade(nums1)
nums2 = [3, 1, 4, 2]
find132pattern_selfmade(nums2)
nums3 = [-1, 3, 2, 0]
find132pattern_selfmade(nums3)


# from sortedcontainers import SortedList
# 这种方法通过枚举132中3的下标来实现
def find132pattern_improved1(nums):
    if len(nums) < 3:
        return False
    length = len(nums)
    left_min = nums[0]
    right_all = SortedList(nums[2:])
    for j in range(1, length - 1):
        if left_min < nums[j]:
            index = right_all.bisect_right(left_min)
            if index < len(right_all) and right_all[index] < nums[j]:
                return True
        left_min = min(left_min, nums[j])
        right_all.remove(nums[j + 1])
    return False


nums1 = [1, 2, 3, 4]
find132pattern_improved1(nums1)
nums2 = [3, 1, 4, 2]
find132pattern_improved1(nums2)
nums3 = [1, 4, 0, -1, -2, -3, -1, -2]
find132pattern_improved1(nums3)


# 这种方法通过枚举132中的1来实现
def find132pattern_improved2(nums):
    if len(nums) < 3:
        return False
    length = len(nums)
    candidates = [nums[length - 1]]
    max_k = float('-inf')
    for j in range(length - 2, -1, -1):
        if nums[j] < max_k:
            return True
        while candidates and nums[j] > candidates[-1]:
            max_k = candidates.pop()
        if nums[j] > max_k:
            candidates.append(nums[j])
    return False


nums1 = [1, 2, 3, 4]
find132pattern_improved2(nums1)
nums2 = [3, 1, 4, 2]
find132pattern_improved2(nums2)
nums3 = [1, 4, 0, -1, -2, -3, -1, -2]
find132pattern_improved2(nums3)


def find132pattern_fromImproved2(nums):
    if len(nums) < 3:
        return False
    length = len(nums)
    dictionary = [[nums[0], float('-inf')]]
    for i in range(1, length):
        if len(dictionary) > 1:
            for j in range(0, len(dictionary) - 1):
                if dictionary[j][0] < nums[i] < dictionary[j][1]:
                    return True
        if nums[i] < dictionary[-1][0]:
            if dictionary[-1][1] == float('-inf'):
                dictionary[-1][0] = nums[i]
            else:
                dictionary.append([nums[i], float('-inf')])
        elif nums[i] > dictionary[-1][1]:
            dictionary[-1][1] = nums[i]
        elif dictionary[-1][0] < nums[i] < dictionary[-1][1]:
            return True
    return False


nums1 = [1, 2, 3, 4]
find132pattern_fromImproved2(nums1)
nums2 = [3, 1, 4, 2]
find132pattern_fromImproved2(nums2)
nums3 = [1, 4, 0, -1, -2, -3, -1, -2]
find132pattern_fromImproved2(nums3)


# 461. 汉明距离
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
def hammingDistance(x, y):
    counter = 0
    x = str(bin(x))[2:]
    y = str(bin(y))[2:]
    x = x.zfill(max(len(x), len(y)))
    y = y.zfill(max(len(x), len(y)))
    for i in range(len(x)):
        counter += not x[i] == y[i]
    return counter


x = 55
y = 123
hammingDistance(x, y)


# 463. 岛屿的周长
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

def islandPerimeter(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                counter += (i - 1 < 0) + (j - 1 < 0) + (i + 1 == len(grid)) + (j + 1 == len(grid[0]))
                if 0 < i < (len(grid) - 1):
                    counter += (not grid[i - 1][j]) + (not grid[i + 1][j])
                if 0 < j < (len(grid[0]) - 1):
                    counter += (not grid[i][j - 1]) + (not grid[i][j + 1])
                if i == 0 and j == len(grid[0]) - 1:
                    counter += (not grid[i][j - 1]) + (not grid[i + 1][j])
                if i == 0 and j == 0:
                    counter += (not grid[0][1]) + (not grid[1][0])
                if i == len(grid) - 1 and j == 0:
                    counter += (not grid[i - 1][j]) + (not grid[i][j + 1])
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    counter += (not grid[i - 1][j]) + (not grid[i][j - 1])
    return counter


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
islandPerimeter(grid)


# 503. 下一个更大元素 II
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
# 这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
def nextGreaterElements_selfmade(nums):
    length = len(nums)
    result = [0] * length
    for i in range(length):
        hasChanged = False
        for j in range(i + 1, i + length + 1):
            if nums[i] < nums[j % length]:
                result[i] = nums[j % length]
                hasChanged = True
                break
        if not hasChanged:
            result[i] = -1
    return result


List = []
for i in range(500000):
    List.append(random.randint(1, 500000))
nums = [1, 2, 1]
start_time = datetime.datetime.now()
result1 = nextGreaterElements_selfmade(List)
end_time = datetime.datetime.now()
print(end_time - start_time)


def nextGreaterElements_recommonded(nums):
    length = len(nums)
    result = [-1] * length
    stack = list()
    for i in range(length * 2 - 1):
        while stack and nums[stack[-1]] < nums[i % length]:
            result[stack.pop()] = nums[i % length]
        stack.append(i % length)
    return result


start_time = datetime.datetime.now()
result2 = nextGreaterElements_recommonded(List)
end_time = datetime.datetime.now()
print(end_time - start_time)


# 530. 二叉搜索树的最小绝对差
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。


def getMinimumDifference(root):
    differences = []
    node = root

    def recursion(node):
        if node.left:
            differences.append(abs(node.left.val - node.val))
            recursion(node.left)
        if node.right:
            differences.append(abs(node.right.val - node.val))
            recursion(node.right)
        return

    recursion(node)
    return min(differences)


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t3
t3.left = t2
getMinimumDifference(t1)
