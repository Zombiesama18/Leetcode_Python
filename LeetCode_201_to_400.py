import datetime
import random


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


# 206. 反转链表
# 反转一个单链表。
def reverseList(head):
    nodelist = []
    while head:
        nodelist.append(head)
        head = head.next
    for i in range(len(nodelist) - 1, 0, -1):
        nodelist[i].next = nodelist[i - 1]
    nodelist[0].next = None
    return nodelist[-1]


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
head = reverseList(l1)
while head:
    print(head.val)
    head = head.next


# 208. 实现 Trie (前缀树)
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
class Trie:

    class Node:
        def __init__(self, value='', isKey=False):
            self.value = value
            self.isKey = isKey
            self.map = {}
            self.numWords = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        self.size = 0

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            current.numWords += 1
            if not current.map.get(char):
                current.map[char] = self.Node(char, False)
            current = current.map.get(char)
        current.isKey = True
        self.size += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return bool(self.get(self.root, word, 0))

    def get(self, x: Node, word: str, depth: int):
        if not x:
            return None
        if depth == len(word):
            if x.isKey:
                return x
            else:
                return None
        char = word[depth]
        return self.get(x.map.get(char), word, depth + 1)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        x = self.subStartWith(self.root, prefix, 0)
        return bool(x)

    def subStartWith(self, x: Node, word: str, depth: int):
        if not x:
            return None
        if depth == len(word):
            return x
        char = word[depth]
        return self.subStartWith(x.map.get(char), word, depth + 1)


# 213. 打家劫舍 II（需要复习）
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
def rob(nums: [int]) -> int:
    def robRange(start: int, end: int):
        first = nums[start]
        second = max(nums[start + 1], first)
        for i in range(start + 2, end + 1):
            first, second = second, max(first + nums[i], second)
        return second

    length = len(nums)
    if length == 0:
        return 0
    if length < 3:
        return max(nums)
    return max(robRange(0, length - 2), robRange(1, length - 1))


# 220. 存在重复元素 III（需要复习）
# 给你一个整数数组 nums 和两个整数k 和 t 。请你判断是否存在两个下标 i 和 j，使得abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
# 如果存在则返回 true，不存在返回 false。
def containsNearbyAlmostDuplicate(nums: [int], k: int, t: int) -> bool:
    length = len(nums)
    numsWindow = {}
    denominator = t + 1
    for i in range(length):
        inputId = nums[i] // denominator
        if inputId in numsWindow:
            return True
        if inputId + 1 in numsWindow and numsWindow[inputId + 1] - nums[i] < denominator:
            return True
        if inputId - 1 in numsWindow and nums[i] - numsWindow[inputId - 1] < denominator:
            return True
        numsWindow[inputId] = nums[i]
        if i >= k:
            numsWindow.pop((nums[i - k]) // denominator)
    return False


# 224. 基本计算器
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
# 自制版本无法完成s = '(-3+2)-(-4+2)'操作
def calculate_selfmade(s: str):
    if not s:
        return 0
    stack_num = [0]
    stack_ope = ['+']

    def sub_calc():
        if len(stack_num) == 1:
            number2 = stack_num.pop()
            stack_num.append(0)
            stack_num.append(number2)
        operator = stack_ope[-1]
        if operator == '+':
            number1 = stack_num.pop()
            stack_ope.pop()
            if stack_ope and stack_ope[-1] == '-':
                stack_num[-1] = stack_num[-1] - number1
            else:
                stack_num[-1] = stack_num[-1] + number1
        elif operator == '-':
            number1 = stack_num.pop()
            stack_ope.pop()
            if stack_ope and stack_ope[-1] == '-':
                stack_num[-1] = stack_num[-1] + number1
            else:
                stack_num[-1] = stack_num[-1] - number1
        return

    def digitMerge():
        number1 = stack_num.pop()
        stack_num[-1] = 10 * stack_num[-1] + number1
        return

    temp = ''
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        elif s[i] == '+' or s[i] == '-' or s[i] == '(':
            stack_ope.append(s[i])
        elif s[i] == ')':
            if stack_ope[-1] == '(':
                stack_ope.pop()
                sub_calc()
            else:
                while stack_ope[-1] != '(':
                    sub_calc()
                stack_ope.pop()
        elif s[i].isdigit():
            if temp.isdigit():
                stack_num.append(int(s[i]))
                digitMerge()
            else:
                if i < len(s) - 1 and s[i + 1].isdigit():
                    stack_num.append(int(s[i]))
                else:
                    stack_num.append(int(s[i]))
                    sub_calc()
        temp = s[i]
    while stack_ope:
        sub_calc()
    return stack_num[-1]


s = "1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10"
s = '(-3+2)-(-4+2)'
calculate_selfmade(s)


def calculate_recommonded(s: str):
    stack_ops = [1]
    sign = 1
    result = 0
    length = len(s)
    i = 0
    while i < length:
        if s[i] == ' ':
            i += 1
        elif s[i] == '+':
            sign = stack_ops[-1]
            i += 1
        elif s[i] == '-':
            sign = -stack_ops[-1]
            i += 1
        elif s[i] == '(':
            stack_ops.append(sign)
            i += 1
        elif s[i] == ')':
            stack_ops.pop()
            i += 1
        else:
            num = 0
            while i < length and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            result += num * sign
    return result


s = "1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10"
calculate_recommonded(s)


# 227. 基本计算器 II
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
def calculate_first(s: str):
    length = len(s)
    sign = 1
    index = 0
    stack_num = list()
    stack_ops = list()
    while index < length:
        if s[index] == ' ' or s[index] == '+':
            index = index + 1
        elif s[index] == '-':
            sign = -sign
            index = index + 1
        elif s[index] == '*' or s[index] == '/':
            stack_ops.append(s[index])
            index = index + 1
        else:
            num = 0
            while index < length and s[index].isdigit():
                num = num * 10 + ord(s[index]) - ord('0')
                index = index + 1
            if stack_ops:
                if stack_ops[-1] == '*':
                    stack_num.append(stack_num.pop() * num)
                if stack_ops[-1] == '/':
                    stack_num.append(int(stack_num.pop() / num))
                stack_ops.pop()
            else:
                stack_num.append(sign * num)
                sign = 1
    return sum(stack_num)


s = "3+2*2"
calculate_first(s)
s = " 3/2 "
calculate_first(s)
s = " 3+5 / 2 "
calculate_first(s)


# 232. 用栈实现队列
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：
# 你只能使用标准的栈操作 —— 也就是只有push to top,peek/pop from top,size, 和is empty操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.reverse = False
        self.size = 0

    def push(self, x):
        if self.reverse:
            for i in range(self.size):
                self.stack1.append(self.stack2.pop())
            self.reverse = False
        self.stack1.append(x)
        self.size += 1

    def pop(self):
        if not self.reverse:
            for i in range(self.size):
                self.stack2.append(self.stack1.pop())
            self.reverse = True
        self.size -= 1
        return self.stack2.pop()

    def peek(self):
        if not self.reverse:
            for i in range(self.size):
                self.stack2.append(self.stack1.pop())
            self.reverse = True
        return self.stack2[-1]

    def empty(self):
        return self.size == 0


myqueue = MyQueue()
myqueue.push(1)
myqueue.push(2)
myqueue.peek()
myqueue.pop()
myqueue.empty()


# 263. 丑数
# 给你一个整数 n1 ，请你判断 n1 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
# 丑数 就是只包含质因数2、3 和/或5的正整数。
def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    while n != 1:
        if n % 5 == 0:
            n = n / 5
        elif n % 3 == 0:
            n = n / 3
        elif n % 2 == 0:
            n = n / 2
        else:
            return False
    return True


# 264. 丑数 II（需要复习）
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
def nthUglyNumber(n: int) -> int:
    uglyNumbers = {1}
    multiplier2 = 1
    multiplier3 = 1
    multiplier5 = 1
    while len(uglyNumbers) < n:
        if 2 * multiplier2 < 3 * multiplier3:
            if multiplier2 in uglyNumbers:
                uglyNumbers.add(2 * multiplier2)
            multiplier2 += 1
        elif 3 * multiplier3 < 5 * multiplier5:
            if multiplier3 in uglyNumbers:
                uglyNumbers.add(3 * multiplier3)
            multiplier3 += 1
        else:
            if multiplier5 in uglyNumbers:
                uglyNumbers.add(5 * multiplier5)
            multiplier5 += 1
    result = list(uglyNumbers)
    result.sort()
    return result[n - 1]


# 309. 最佳买卖股票时机含冷冻期
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#     你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#     卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
def maxProfit(prices):
    operation_dict = {0: '按兵不动', 1: '买入', 2: '卖出', 3: '冷冻期'}
    profit_list = []
    history_list = []

    def recursion(day, operation, profit, history, state_buyin):
        if day == len(prices) - 1:
            profit_list.append(profit)
            history_list.append(history[:])
            return
        if operation == 0 or operation == 3:
            if state_buyin:
                recursion(day + 1, 0, profit, history + [0], state_buyin)
                recursion(day + 1, 2, profit + prices[day + 1], history + [2], not state_buyin)
            else:
                recursion(day + 1, 0, profit, history + [0], state_buyin)
                recursion(day + 1, 1, profit - prices[day + 1], history + [1], not state_buyin)
        if operation == 1:
            state_buyin = True
            recursion(day + 1, 0, profit, history + [0], state_buyin)
            recursion(day + 1, 2, profit + prices[day + 1], history + [2], not state_buyin)
        if operation == 2:
            state_buyin = False
            recursion(day + 1, 3, profit, history + [3], state_buyin)

    recursion(0, 0, 0, [0], False)
    recursion(0, 1, -prices[0], [1], True)
    name_list = []
    for i in history_list[profit_list.index(max(profit_list))]:
        name_list.append(operation_dict[i])
    return name_list


prices = [1, 2, 3, 0, 2]
maxProfit(prices)


# 312. 戳气球
# 有 n1 个气球，编号为0 到 n1-1，每个气球上都标有一个数字，这些数字存在数组 nums1 中。
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums1[left] * nums1[i] * nums1[right] 个硬币。
# 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 求所能获得硬币的最大数量。
def maxCoins(nums):
    values = []

    def recursion(temp, counter):
        if len(temp) == 2:
            counter += temp[0] * temp[1] + max(temp)
            values.append(counter)
            return
        recursion(temp[1:], counter + temp[0] * temp[1])
        for i in range(1, len(temp) - 1):
            recursion(temp[:i] + temp[i + 1:], counter + (temp[i - 1] * temp[i] * temp[i + 1]))
        recursion(temp[:-1], counter + temp[-2] * temp[-1])

    recursion(nums, 0)
    return max(values)


nums = [3, 1, 5, 8]
maxCoins(nums)


# 331. 验证二叉树的前序序列化（需要复习）
# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# 例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
# 给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
# 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
# 你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如"1,,3" 。
# 解答：
# 我们可以定义一个概念，叫做槽位。一个槽位可以被看作「当前二叉树中正在等待被节点填充」的那些位置。二叉树的建立也伴随着槽位数量的变化。每当遇到一个节点时：
# 如果遇到了空节点，则要消耗一个槽位；如果遇到了非空节点，则除了消耗一个槽位外，还要再补充两个槽位。此外，还需要将根节点作为特殊情况处理。
# 我们使用栈来维护槽位的变化。栈中的每个元素，代表了对应节点处剩余槽位的数量，而栈顶元素就对应着下一步可用的槽位数量。当遇到空节点时，
# 仅将栈顶元素减 11；当遇到非空节点时，将栈顶元素减 11 后，再向栈中压入一个 22。无论何时，如果栈顶元素变为 00，就立刻将栈顶弹出。
# 遍历结束后，若栈为空，说明没有待填充的槽位，因此是一个合法序列；否则若栈不为空，则序列不合法。此外，在遍历的过程中，若槽位数量不足，则序列不合法。
def isValidSerialization(preorder: str):
    preorder = preorder.split(',')
    length = len(preorder)
    stack = [1]
    for i in range(length):
        if not stack:
            return False
        if preorder[i] == '#':
            top = stack.pop() - 1
            if top > 0:
                stack.append(top)
        else:
            top = stack.pop() - 1
            if top > 0:
                stack.append(top)
            stack.append(2)
    return not stack


preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
isValidSerialization(preorder)
preorder = "1"
isValidSerialization(preorder)
preorder = "9,#,#,1"
isValidSerialization(preorder)


# 322. 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。
# 遍历方法
# def coinChange(coins, amount):
#     values = []
#
#     def recursion(history, money):
#         if money == amount:
#             values.append(history[:])
#             return
#         if money > amount:
#             return
#         for i in coins:
#             recursion(history + [i], money + i)
#
#     recursion([], 0)
#     if values:
#         return max(values)
#     else:
#         return -1
# 最大值方法
def coinChange(coins, amount):
    money = 0
    counter = 0
    while money < amount:
        if not coins:
            return -1
        if money + max(coins) > amount:
            coins.remove(max(coins))
        else:
            temp = max(coins)
            money += temp
            counter += 1
    return counter


coins = [1, 2, 5]
amount = 11
coinChange(coins, amount)


# 338. 比特位计数
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
def countBits_exhaustion(num):
    def count1(s):
        counter = 0
        for j in s:
            if j == '1':
                counter += 1
        return counter

    output = []
    for i in range(num + 1):
        number = bin(i)[2:]
        output.append(count1(number))
    return output


countBits_exhaustion(5)


def countBits_simple(num):
    result = list(range(num + 1))
    if num == 0:
        return result
    if num == 1:
        return result
    result[2] = 1
    if num == 2:
        return result
    for i in range(3, num + 1):
        if i % 2 == 0:
            result[i] = result[int(i / 2)]
        else:
            result[i] = result[int((i - 1) / 2)] + 1
    return result


countBits_simple(16)


# 341. 扁平化嵌套列表迭代器（需要复习）
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
class NestedInteger:

    def isInteger(self):
        pass

    def getInterger(self):
        pass

    def getList(self):
        pass


class NestedIterator_withIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.result = list()
        self.dfs(self.nestedList.getList())
        self.iterator = self.result.__iter__()
        self.output = int

    def dfs(self, nestList):
        for nest in nestList:
            if nest.isInteger():
                self.result.append(nest)
            else:
                self.dfs(nest.getList())

    def next(self):
        return self.output

    def hasNext(self):
        try:
            self.output = self.iterator.__next__()
        except StopIteration:
            return False
        else:
            return True


class NestedIterator_withIndex:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.result = list()
        self.dfs(self.nestedList)
        self.index = 0
        self.length = len(self.result)

    def dfs(self, nestList):
        for nest in nestList:
            if nest.isInteger():
                self.result.append(nest)
            else:
                self.dfs(nest.getList())

    def next(self):
        temp = self.result[self.index]
        self.index += 1
        return temp

    def hasNext(self):
        return self.index < self.length
# 344. 反转字符串
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
# 得到启发：左右指针


# def reverseString(s):
#     left = 0
#     right = len(s) - 1
#     s = list(s)
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#     return ''.join(s)


def reverseString(s):
    s = list(s)
    s.reverse()
    return ''.join(s)


reverseString('hello')


# 347. 前 K 个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
def topKFrequent(nums, k):
    temp = set(nums)
    temp_dict = {}
    for i in temp:
        times = nums.count(i)
        if times in temp_dict:
            temp_value = [temp_dict[times], i]
            temp_dict[times] = temp_value
        else:
            temp_dict[times] = i
    frequence = list(temp_dict.keys())
    frequence.sort()
    frequence.reverse()
    output = []
    for i in range(k):
        output.append(temp_dict[frequence[i]])
    return output


nums = [1, 1, 1, 2, 2, 3, 3]
k = 2
topKFrequent(nums, k)

# 354. 俄罗斯套娃信封问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式(w, h)出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 说明:
# 不允许旋转信封。
List = []
for i in range(10000):
    List.append([random.randint(1, 10000), random.randint(1, 10000)])


def maxEnvelopes_recommended(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


start_time = datetime.datetime.now()
maxEnvelopes_recommended(List)
end_time = datetime.datetime.now()
print(end_time - start_time)


# 394. 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
def decodeString(s):
    output = ''
    group = s.split(']')

    def recursion(temp):
        if temp == '':
            return ''
        if temp[0].isdigit():
            times = int(temp[0: temp.index('[')])
            subcomb = recursion(temp[temp.index('[') + 1:])
            return subcomb * times
        if temp[0].isalpha():
            if '[' in temp:
                word = temp[0: temp.index('[') - 1]
                return word + recursion(temp[temp.index('[') - 1:])
            else:
                return temp

    for i in group:
        output += recursion(i)
    return output


s = "2[abc]3[cd]ef"
decodeString(s)


# 399. 除法求值
# 给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。
# 输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
def calcEquation(equations, values, queries):
    all_possible = equations[:]
    for i in range(len(equations) - 1):
        for j in range(i + 1, len(equations)):
            if equations[i][1] == equations[j][0]:
                all_possible.append([equations[i][0], equations[j][1]])
                values.append(values[i] * values[j])
            if equations[i][0] == equations[j][0]:
                all_possible.append([equations[j][1], equations[i][1]])
                values.append(values[i] / values[j])
    temp = all_possible[:]
    for i in range(len(all_possible)):
        temp_list = all_possible[i][:]
        temp_list.reverse()
        temp.append(temp_list)
        values.append(1 / values[i])
    output = []
    for i in range(len(queries)):
        if queries[i] in temp:
            output.append(values[temp.index(queries[i])])
        else:
            output.append(-1.0)
    return output


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
calcEquation(equations, values, queries)
