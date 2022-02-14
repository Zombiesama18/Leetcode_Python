import collections
from libraries import Tree


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


def generateTreebyLevelOrder(levelOrder):
    length = len(levelOrder)
    nodeList = list()
    for item in levelOrder:
        if not item:
            nodeList.append(None)
        else:
            nodeList.append(TreeNode(item))
    for i in range(length):
        if 2 * i + 2 > length - 1:
            break
        nodeList[i].left = nodeList[2 * i + 1]
        nodeList[i].right = nodeList[2 * i + 2]
    return nodeList[0]


def inorderTravesal(root):
    result = []

    def subInorderTraversal(node):
        if not node:
            return
        subInorderTraversal(node.left)
        result.append(node.val)
        subInorderTraversal(node.right)
        return

    subInorderTraversal(root)
    return result


# 152. 乘积最大子数组
# 给你一个整数数组 nums1 ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
def maxProduct(nums):
    subsets = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subsets.append(nums[i:j])
    output = []
    for i in subsets:
        temp = 1
        for j in i:
            temp = temp * j
        output.append(temp)
    return max(output)


nums = [2, 3, -2, 4]
maxProduct(nums)
nums = [-2, 0, -1]
maxProduct(nums)


# 153. 寻找旋转排序数组中的最小值
# 已知一个长度为 n1 的数组，预先按照升序排列，经由 1 到 n1 次 旋转 后，得到输入数组。
# 例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 4 次，则可以得到 [0,1,2,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n1-1]] 旋转一次 的结果为数组 [a[n1-1], a[0], a[1], a[2], ..., a[n1-2]] 。
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
def findMin(nums: [int]) -> int:
    if not nums:
        return nums
    length = len(nums)
    if length == 1:
        return nums[0]
    for i in range(length - 1):
        if nums[i] < nums[-1]:
            return nums[i]
    return nums[-1]


# 154. 寻找旋转排序数组中的最小值 II
def findMinVersion2(nums: [int]) -> int:
    if not nums:
        return nums
    length = len(nums)
    if length == 1:
        return nums[0]
    left, right = 0, length - 1
    while left < right:
        pivot = (left + right) >> 1
        if nums[pivot] < nums[right]:
            right = pivot
        elif nums[pivot] > nums[right]:
            left = pivot + 1
        else:
            right -= 1
    return nums[left]


# 155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
class MinStack:

    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        self.values.pop(-1)

    def top(self):
        return self.values[-1]

    def getMin(self):
        return min(self.values)


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()


# 160. 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。
def getIntersectionNode(headA, headB):
    temp = headA
    while headB:
        while headA:
            if headA.next == headB:
                return headA.next.val
            headA = headA.next
        headA = temp
        headB = headB.next
    return None


l1 = ListNode(4)
l2 = ListNode(1)
l3 = ListNode(5)
l4 = ListNode(0)
l5 = ListNode(1)
l6 = ListNode(8)
l7 = ListNode(4)
l8 = ListNode(5)
l1.next = l2
l2.next = l6
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
getIntersectionNode(l1, l3)
l1 = ListNode(0)
l2 = ListNode(9)
l3 = ListNode(1)
l4 = ListNode(3)
l5 = ListNode(2)
l6 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l5
l4.next = l5
l5.next = l6
getIntersectionNode(l1, l4)
l1 = ListNode(0)
l2 = ListNode(9)
l3 = ListNode(1)
l4 = ListNode(3)
l5 = ListNode(2)
l1.next = l2
l2.next = l3
l4.next = l5
getIntersectionNode(l1, l4)


# 169. 多数元素
# 给定一个大小为 n1 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n1/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
def majorityElement(nums):
    length = len(nums)
    history = []
    for i in nums:
        if i not in history:
            history.append(i)
            if nums.count(i) > (length / 2):
                return i
    return 'No Majoritylement'


nums = [3, 2, 3]
majorityElement(nums)
nums = [2, 2, 1, 1, 1, 2, 2]
majorityElement(nums)


# 173. 二叉搜索树迭代器
# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于
# BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
# 你可以假设next()调用总是有效的，也就是说，当调用 next()时，BST 的中序遍历中至少存在一个下一个数字。
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.inOrder = list()
        self.inOrderTraversal(root)
        self.index = 0
        self.length = len(self.inOrder)

    def inOrderTraversal(self, node):
        if not node:
            return
        self.inOrderTraversal(node.left)
        self.inOrder.append(node.val)
        self.inOrderTraversal(node.right)
        return

    def next(self) -> int:
        temp = self.inOrder[self.index]
        self.index += 1
        return temp

    def hasNext(self) -> bool:
        return self.index < self.length


levelOrder = [7, 3, 15, None, None, 9, 20]
root = generateTreebyLevelOrder(levelOrder)
inorderTravesal(root)


# 179. 最大数
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
def largestNumberPracticeofMergeSort(nums: [int]) -> str:
    def getMax(q1: deque, q2: deque):
        if len(q1) == 0:
            return q2.popleft()
        elif len(q2) == 0:
            return q1.popleft()
        else:
            if compareTo(q1[0], q2[0]):
                return q1.popleft()
            else:
                return q2.popleft()

    def compareTo(s1: str, s2: str):
        return s1 + s2 > s2 + s1

    dq = deque()
    for num in nums:
        dq.append(deque([str(num)]))
    while len(dq) != 1:
        q1 = dq.popleft()
        q2 = dq.popleft()
        temp = deque()
        while len(q1) != 0 or len(q2) != 0:
            temp.append(getMax(q1, q2))
        dq.append(temp)
    result = ''.join(dq.pop())
    if result[0] == '0':
        result = '0'
    return result


# 190. 颠倒二进制位
# 颠倒给定的 32 位无符号整数的二进制位。
# 提示：
# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，
# 因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的示例 2中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。
# 示例 2：
# 输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
# 因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。
def reverseBits(n: int):
    return int(bin(n)[2:].zfill(32)[::-1], 2)


def reverseBitsbyBit(n):
    result = 0
    counter = 0
    while counter < 32 and n != 0:
        result |= (n & 1) << (31 - counter)  # n1 & 1 是最低位与， << 向左移位 (31-counter)位
        n >>= 1
        counter += 1
    return result


n = 0b00000010100101000001111010011100
reverseBitsbyBit(n)


# 191. 位1的个数
# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
# 提示：
# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，
# 因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的示例 3中，输入表示有符号整数 -3。
# 示例 3：
# 输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
def hammingWeight_simple(n: int):
    return bin(n).count('1')


n1 = 0b00000000000000000000000000001011
hammingWeight_simple(n1)
n2 = 0b00000000000000000000000010000000
hammingWeight_simple(n2)
n3 = 11111111111111111111111111111101
hammingWeight_simple(n3)


# 位运算
# 思路及解法
# 观察这个运算：n1 & (n1 - 1)，其预算结果恰为把 n1 的二进制位中的最低位的 1 变为 0 之后的结果。
# 如：6 & (6 - 1) = 4, 6 = (110)_2, 4 = (100)_2，运算结果 4 即为把 6 的二进制位中的最低位的 1 变为 0 之后的结果。

def hammingWeight_bitComputation(n: int):
    result = 0
    while n != 0:
        n = n & (n - 1)
        result += 1
    return result


n1 = 0b00000000000000000000000000001011
hammingWeight_bitComputation(n1)
n2 = 0b00000000000000000000000010000000
hammingWeight_bitComputation(n2)
n3 = 11111111111111111111111111111101
hammingWeight_bitComputation(n3)


# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
def rob(nums):
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)
    cashWithDistanceOf2 = nums[0]
    cashWithDistanceOf1 = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        cashWithDistanceOf2, cashWithDistanceOf1 = cashWithDistanceOf1, max(cashWithDistanceOf2 + nums[i], cashWithDistanceOf1)
    return cashWithDistanceOf1


# 200. 岛屿数量（需要复习）
# 给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
# 用一个等大的矩阵来表示有没有访问过
def numIslands(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                grid[i][j] = '0'  # 表示访问过
                counter += 1
                land_posits = collections.deque()
                land_posits.append([i, j])
                while len(land_posits) > 0:  # 遍历出一整块陆地
                    x, y = land_posits.popleft()
                    for new_x, new_y in ([x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]):
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                            # 如果新的xy在grid里而且对应地点也是陆地
                            grid[new_x][new_y] = '0'
                            land_posits.append([new_x, new_y])
    return counter


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
numIslands(grid)
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
numIslands(grid)
