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


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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


# 101. 对称二叉树（需要复习）
# 给定一个二叉树，检查它是否是镜像对称的。

# 一个思路是得到中序遍历，看结果是否对称
# def isSymmetric(root):
#     values = inorderTraversal(root)
#     if values[::-1] == values:
#         return True
#     else:
#         return False

# 一般思路是从根节点的左节点和右节点分别开始做文章。
def isSymmetric(root):
    def recursion(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return recursion(left.left, right.right) and recursion(left.right, right.left)

    return recursion(root.left, root.right)


l1 = TreeNode(3)
l2 = TreeNode(2)
l3 = TreeNode(4)
l4 = TreeNode(1)
l5 = TreeNode(2)
l6 = TreeNode(4)
l7 = TreeNode(3)
l4.left = l2
l2.left = l1
l2.right = l3
l4.right = l5
l5.left = l6
l5.right = l7
isSymmetric(l4)
l1 = TreeNode(2)
l2 = TreeNode(3)
l3 = TreeNode(1)
l4 = TreeNode(2)
l5 = TreeNode(3)
l3.left = l1
l1.right = l2
l3.right = l4
l4.right = l5
isSymmetric(l3)


# 102. 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

def levelOrder(root):
    values = []

    def recursion(node, layer):
        if len(values) < layer + 1:
            values.append([])
        values[layer].append(node.val)
        if not node.left and not node.right:
            return
        if node.left:
            recursion(node.left, layer + 1)
        if node.right:
            recursion(node.right, layer + 1)
        return

    recursion(root, 0)
    return values


l1 = TreeNode(3)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)
l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5
levelOrder(l1)


# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。

def maxDepth(root):
    depths = []

    def recursion(node, depth):
        if not node.left and not node.right:
            depths.append(depth)
            return
        if node.left:
            recursion(node.left, depth + 1)
        if node.right:
            recursion(node.right, depth + 1)
        return

    recursion(root, 1)
    return max(depths)


l1 = TreeNode(3)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)
l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5
maxDepth(l1)


# 105. 从前序与中序遍历序列构造二叉树（需要复习）
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。

def buildTree(preorder, inorder):
    if not preorder and not inorder:
        return
    root = TreeNode(preorder[0])
    ind = inorder.index(root.val)
    root.left = buildTree(preorder[1: ind + 1], inorder[:ind])
    root.right = buildTree(preorder[ind + 1:], inorder[ind + 1:])
    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
buildTree(preorder, inorder)


# 114. 二叉树展开为链表
# 给定一个二叉树，原地将它展开为一个单链表。
# 前序遍历

def flatten(root):
    values = []

    def recursion(now):
        values.append(now.val)
        if not now.left and not now.right:
            return
        if now.left:
            recursion(now.left)
        if now.right:
            recursion(now.right)
        return

    recursion(root)
    nodelist = [ListNode(0) for _ in range(len(values))]
    for i in range(len(values) - 1, 0, -1):
        nodelist[i].val = values[i]
        nodelist[i - 1].val = values[i - 1]
        nodelist[i - 1].next = nodelist[i]
    return nodelist[0]


l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(6)
l1.left = l2
l2.left = l3
l2.right = l4
l1.right = l5
l5.right = l6
head = flatten(l1)
print(head.val)
head = head.next
while head:
    print(' -> ', head.val)
    head = head.next


# 115. 不同的子序列（需要复习）
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）
# 题目数据保证答案符合 32 位带符号整数范围。
# 疑问：为什么"rabbb"中"rab"的个数等于"rabb"中"rab"的个数加"rabb"中"ra"的个数
def numDistinct(s: str, t: str):
    if not s or not t or len(t) > len(s):
        return 0
    dp = [[0] * len(s) for _ in range(len(t))]
    dp[0][0] = int(s[0] == t[0])
    for j in range(1, len(s)):
        if s[j] == t[0]:
            dp[0][j] = dp[0][j - 1] + 1
        else:
            dp[0][j] = dp[0][j - 1]
    for i in range(1, len(t)):
        for j in range(len(s)):
            if j < i:
                continue
            if t[i] == s[j]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


s = "rabbbit"
t = "rabbit"
numDistinct(s, t)
s = "babgbag"
t = "bag"
numDistinct(s, t)


# 116. 填充每个节点的下一个右侧节点指针（需要复习）
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有next 指针都被设置为 NULL。
# 得到每一层的节点
def connect(root):
    queue = [root]
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if i < size - 1:
                node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
l6 = Node(6)
l7 = Node(7)
l1.left = l2
l1.right = l3
l2.left = l4
l2.right = l5
l3.left = l6
l3.right = l7
head = connect(l1)
head.left.next.val


# 121. 买卖股票的最佳时机
# 给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。

def maxProfit(prices):
    buy_in = min(prices)
    ind = prices.index(buy_in)
    if prices[ind + 1:]:
        return max(prices[ind + 1:]) - buy_in
    else:
        return 0


prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)
prices = [7, 6, 4, 3, 1]
maxProfit(prices)


# 124. 二叉树中的最大路径和
# 给定一个非空二叉树，返回其最大路径和。
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

def maxPathSum(root):
    values = []
    nodelist = []

    def get_values(now):
        values.append(now.val)
        nodelist.append(now)
        if not now.left and not now.right:
            return
        if now.left:
            get_values(now.left)
        if now.right:
            get_values(now.right)
        return

    def is_connected(now, nums):
        nums.remove(now.val)
        if not nums:
            return True
        if not now.left and not now.right:
            return False
        if now.left:
            if now.left.val in nums:
                flag = is_connected(now.left, nums)
            else:
                return False
        if now.right:
            if now.right.val in nums:
                flag = is_connected(now.right, nums)
            else:
                return flag
        return flag

    get_values(root)
    seqs = []
    for i in range(len(values)):
        for j in range(i + 1, len(values) + 1):
            if len(values[i:j]) > 1:
                if is_connected(nodelist[i], values[i:j]):
                    seqs.append(values[i:j])
            else:
                seqs.append(values[i:j])
    sum_seq = []
    for i in range(len(seqs)):
        sum_seq.append(sum(seqs[i]))
    return max(sum_seq)


l1 = TreeNode(-10)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)
l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5
maxPathSum(l1)


# 128. 最长连续序列（需要复习）
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n1)。
# 思路一：求出所有序列后算长度
# def longestConsecutive(nums1):
#     nums1.sort()
#     output = []
#     counter = 0
#     flag = True
#     for i in range(1, len(nums1)):
#         if len(output) == counter:
#             output.append([])
#         if nums1[i] == nums1[i - 1] + 1:
#             if flag:
#                 output[counter].append(nums1[i - 1])
#                 output[counter].append(nums1[i])
#                 flag = False
#             else:
#                 output[counter].append(nums1[i])
#         else:
#             flag = True
#             counter += 1
#     lengths = []
#     for i in output:
#         lengths.append(len(i))
#     return max(lengths)
def longestConsecutive(nums):
    nums.sort()
    res = 0
    for num in nums:
        if num - 1 in nums:
            temp = 1
            num = num - 1
            while num + 1 in nums:
                num += 1
                temp += 1
            res = max(res, temp)
    return res


nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)


# 131. 分割回文串（需要复习）
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
def partition(s: str):
    if not s:
        return []
    result = []

    def backtrack(s, temp, result):
        if not s:
            result.append(temp[:])
            return
        for i in range(1, len(s) + 1):
            if s[: i] == s[i - 1:: -1]:
                temp.append(s[: i])
                backtrack(s[i:], temp, result)
                temp.pop()

    backtrack(s, [], result)
    return result


s = 'aab'
partition(s)


# 132.分割回文串 II
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 返回符合要求的 最少分割次数 。
def minCut_initial(s: str):
    if not s:
        return []
    result = []

    def backtrack(s, temp, result):
        if not s:
            result.append(temp[:])
            return
        for i in range(1, len(s) + 1):
            if s[: i] == s[i - 1:: -1]:
                temp.append(s[: i])
                backtrack(s[i:], temp, result)
                temp.pop()

    backtrack(s, [], result)
    return len(min(result, key=lambda x: len(x))) - 1


letters = string.ascii_letters[5:13]
s = ''
for i in range(50):
    s = s + random.choice(letters)
start_time = datetime.datetime.now()
result1 = minCut_initial(s)
end_time = datetime.datetime.now()
print(end_time - start_time)


def minCut_third(s: str):
    if not s:
        return None
    if len(s) == 1:
        return 0
    length = len(s)
    dp = [float('inf')] * length
    for i in range(length):
        if s[:i + 1] == s[i:: -1]:
            dp[i] = 0
        else:
            for j in range(i):
                if s[j + 1: i + 1] == s[i: j: -1]:
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]


minCut_third(s)


# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明:
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
def singleNumber(nums):
    history = []
    for num in nums:
        if num not in history:
            if nums.count(num) == 1:
                return num
            history.append(num)
    return 'None'


nums = [2, 2, 1]
singleNumber(nums)
nums = [4, 1, 2, 1, 2]
singleNumber(nums)


# 139. 单词拆分
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 说明：
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
def wordBreak(s, wordDict):
    for word in wordDict:
        if word in s:
            s = s.replace(word, '')
        else:
            return False
    if s:
        return False
    else:
        return True


s = "leetcode"
wordDict = ["leet", "code"]
wordBreak(s, wordDict)
s = "applepenapple"
wordDict = ["apple", "pen"]
wordBreak(s, wordDict)
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
wordBreak(s, wordDict)


# 141. 环形链表
# 给定一个链表，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。


def hasCycle(head):
    history = []
    while head:
        if head in history:
            return True
        history.append(head)
        head = head.next
    return False


l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2
hasCycle(l1)
l1 = ListNode(-1)
hasCycle(l1)


# 142. 环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 说明：不允许修改给定的链表。


def detectCycle(head):
    nodelist = []
    while head:
        if head in nodelist:
            return 'tail connects to node index ' + str(nodelist.index(head))
        nodelist.append(head)
        head = head.next
    return 'no cycle'


l4 = ListNode(-4)
l3 = ListNode(0, l4)
l2 = ListNode(2, l3)
l1 = ListNode(3, l2)
l4.next = l2
detectCycle(l1)
l1 = ListNode(1)
detectCycle(l1)


# 146. LRU缓存机制
# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
# 当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.inner_dict = {}

    def get(self, key):
        if key in self.inner_dict.keys():
            value = self.inner_dict.pop(key)
            self.inner_dict[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if len(self.inner_dict) == self.capacity:
            self.inner_dict.pop(list(self.inner_dict.keys())[0])
        self.inner_dict[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)


# 148. 排序链表（需要学习）
# 在 O(n1 log n1) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 归并排序
def sortList(head):
    pass


# 150. 逆波兰表达式求值
# 根据 逆波兰表示法，求表达式的值。
# 有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
def evalRPN(tokens):
    if not tokens:
        return 0
    stackNum = list()
    for token in tokens:
        if token.isdigit():
            stackNum.append(int(token))
        elif token[1:].isdigit():
            stackNum.append(int(token))
        elif token == '+':
            stackNum.append(stackNum.pop() + stackNum.pop())
        elif token == '-':
            tempNum = stackNum.pop()
            stackNum.append(stackNum.pop() - tempNum)
        elif token == '*':
            stackNum.append(stackNum.pop() * stackNum.pop())
        elif token == '/':
            tempNum = stackNum.pop()
            stackNum.append(int(stackNum.pop() / tempNum))
    return stackNum[0]


tokens = ["2", "1", "+", "3", "*"]
evalRPN(tokens)
tokens = ["4", "13", "5", "/", "+"]
evalRPN(tokens)
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evalRPN(tokens)


def RPN2NE(tokens):
    stackNum = list()
    for token in tokens:
        if token.isdigit():
            stackNum.append(token)
        elif token[1:].isdigit():
            stackNum.append(token)
        elif token == '+' or token == '-':
            temp = stackNum.pop()
            stackNum.append('(' + stackNum.pop() + token + temp + ')')
        elif token == '*' or token == '/':
            temp = stackNum.pop()
            stackNum.append(stackNum.pop() + token + temp)
    return stackNum[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
RPN2NE(tokens)
