import datetime
import random
import string
from libraries.utils import ListNode, traverseListNode, generateListNode
# 1. 两数之和
# 给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


def twoSumByHashTable(nums, target):
    hashMap = dict()
    for i in range(0, len(nums)):
        if target - nums[i] in hashMap:
            return [hashMap[target - nums[i]], i]
        hashMap[nums[i]] = i
    return []


# 2. 两数相加
# 给出两个非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0开头。
def addTwoNumbersIntegreted(l1: ListNode, l2: ListNode):
    root = ListNode(0)
    currentNode = root
    carryBit = 0
    while l1 or l2 or carryBit:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        addResult = l1Val + l2Val + carryBit
        carryBit = addResult // 10
        currentNode.next = ListNode(addResult % 10)
        currentNode = currentNode.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return root.next


# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
def lengthOfLongestSubstringByDict(s):
    subString = dict()
    result = 0
    for i in range(len(s)):
        if s[i] in subString:
            result = max(result, len(subString))
            for char in list(subString.keys()):
                if subString[char] <= subString[s[i]]:
                    subString.pop(char)
                    if char == s[i]:
                        break
        subString[s[i]] = i
    return max(result, len(subString))


# 4. 寻找两个正序数组的中位数
# 给定两个大小为 m 和 n1 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
def findMedianSortedArrays(nums1, nums2):
    nums1 = nums1 + nums2
    nums1.sort()
    if len(nums1) % 2 == 0:
        return float((nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2)
    else:
        return float(nums1[int((len(nums1) - 1) / 2)])


# 5. 最长回文子串（需要复习）
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
def longestPalindrome_selfmade(s):
    result = str()
    lengths = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if i - 1 < 0:
                if s[i: j] == s[j - 1:: -1] and (j - i) > lengths:
                    lengths = j - i
                    result = s[i: j]
            else:
                if s[i: j] == s[j - 1: i - 1: -1] and (j - i) > lengths:
                    lengths = j - i
                    result = s[i: j]
    return result


def longestPalindrome_improved(s):
    if len(s) < 2:
        return s
    length = len(s)
    dp = [[False] * length for _ in range(length)]
    result = ''
    for i in range(length):
        dp[i][i] = True
    for j in range(1, length):
        for i in range(0, j + 1):
            if j == i:
                dp[i][j] = True
            elif j - i == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and j - i + 1 > len(result):
                result = s[i: j + 1]
    return result


letters = string.ascii_letters[5:10]
s = ''
for i in range(1000):
    s = s + random.choice(letters)
start_time = datetime.datetime.now()
longestPalindrome_selfmade(s)
end_time = datetime.datetime.now()
print(end_time - start_time)
start_time = datetime.datetime.now()
longestPalindrome_improved(s)
end_time = datetime.datetime.now()
print(end_time - start_time)


# 10. 正则表达式匹配 （需要复习）
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

# 思路：主要问题是s和p的对齐问题，在p的基础上向s对齐是比较困难的。所以需要另外的状态数组来实现对齐。采取从前传播到后的方法。
# 0代表为空的情况


def isMatch(s, p):
    judge = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
    judge[0][0] = True
    # s和p均为空，结果为True。s为空p非空，若为 字母+* 的格式，也为True。
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*' and judge[0][i - 2]:
            judge[0][i] = True
    # 如果在某个位置上s=p，或p为'.'，则要看之前的状态。
    # 否则如果p='*'，要看前一位，如果前一位不相等且不是'.'，则为False。
    # 如果前一位相等，或为'.'。则要分'*'表示0次，1次和多次前一位。
    # 0次，'a'和'aa*'，当前位状态和两位前相同。
    # 1次，'aa'和'aa*'，当前为状态和前一位相同
    # 多次，'aaa'和'a*'，也是和前一位相同。
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                judge[i][j] = judge[i - 1][j - 1]
            elif p[j - 1] == '*':
                if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                    judge[i][j] = judge[i][j - 2]
                else:
                    judge[i][j] = judge[i][j - 2] or judge[i][j - 1] or judge[i - 1][j]
            else:
                judge[i][j] = False
    return judge[-1][-1]


s = "mississippi"
p = "mis*is*p*."
isMatch(s, p)


# 11. 盛最多水的容器
# 给你 n1 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n1 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且n的值至少为 2。
def maxArea(height):
    area = 0
    for i in range(len(height) - 1):
        for j in range(i, len(height)):
            area = max(((j - i) * min([height[j], height[i]])), area)
    return area


# 15. 三数之和
# 给你一个包含 n1 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
def threeSum(nums):
    result = []
    if len(nums) < 3:
        return result
    nums.sort()
    numsDict = dict()
    for num in nums:
        if num in numsDict:
            numsDict[num] += 1
        else:
            numsDict[num] = 1
    for i in range(len(nums) - 2):
        temp = numsDict.copy()
        for index in range(i + 1):
            if temp[nums[index]] == 1:
                temp.pop(nums[index])
            else:
                temp[nums[index]] -= 1
        for j in range(i + 1, len(nums) - 1):
            if temp[nums[j]] == 1:
                temp.pop(nums[j])
            else:
                temp[nums[j]] -= 1
            if -(nums[i] + nums[j]) in temp:
                if [nums[i], nums[j], -(nums[i] + nums[j])] not in result:
                    result.append([nums[i], nums[j], -(nums[i] + nums[j])])
    return result


# 17. 电话号码的字母组合（需要复习）
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 不定长的循环就用递归
def letterCombinationsFaster(digits):
    if not digits:
        return list()
    letter_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []

    def combinationHelper(combination: str, word: str, depth: int):
        if depth == len(word):
            result.append(combination)
            return
        for char in letter_dict[word[depth]]:
            combinationHelper(combination + char, word, depth + 1)

    combinationHelper('', digits, 0)
    return result


# 19. 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n1 个节点，并且返回链表的头结点。
def removeNthFromEnd(head: ListNode, n: int):
    nodelist = [ListNode(0)]
    nodelist[0].next = head
    while head:
        nodelist.append(head)
        head = head.next
    nodelist[- n - 1].next = nodelist[- n].next
    return nodelist[0].next


# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
def isValid(s):
    stack = []
    str_dict = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in str_dict.keys() and stack and str_dict[i] == stack:
            stack.pop(-1)
        else:
            stack.append(i)
    return not stack


# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
def mergeTwoLists(l1: ListNode, l2: ListNode):
    if not l1:
        return l2
    if not l2:
        return l1
    sentinel = ListNode('0')
    currentNode = sentinel
    while l1 or l2:
        if not l1:
            currentNode.next = l2
            l2 = l2.next
        elif not l2:
            currentNode.next = l1
            l1 = l1.next
        elif l1.val < l2.val:
            currentNode.next = l1
            l1 = l1.next
        else:
            currentNode.next = l2
            l2 = l2.next
        currentNode = currentNode.next
    return sentinel.next


# 22. 括号生成（需要复习）
# 数字 n1 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
def generateParenthesis(n: int):
    result = []

    def generateHelper(combination: str, leftBrace: int, rightBrace: int):
        if leftBrace == 0 and rightBrace == 0:
            result.append(combination)
            return
        if leftBrace > 0:
            generateHelper(combination + '(', leftBrace - 1, rightBrace)
        if leftBrace < rightBrace:
            generateHelper(combination + ')', leftBrace, rightBrace - 1)
        return

    generateHelper('', n, n)
    return result


# 23. 合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
def mergeKListsByFlattening(lists: [ListNode]):
    nodelist = []
    for i in lists:
        while i:
            nodelist.append(i)
            i = i.next

    def getval(node):
        return node.val

    nodelist.sort(key=getval)
    for i in range(len(nodelist) - 1):
        nodelist[i].next = nodelist[i + 1]
    if nodelist:
        return nodelist[0]
    else:
        return None


# 24. 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
def swapPairs(head):
    nodelist = []
    while head:
        nodelist.append(head)
        head = head.next
    while nodelist:
        if len(nodelist) > 3:
            last_one_node = nodelist[-1]
            last_two_node = nodelist[-2]
            last_three_node = nodelist[-3]
            temp = last_one_node.next
            last_three_node.next = last_one_node
            last_one_node.next = last_two_node
            last_two_node.next = temp
            nodelist.pop(-1)
            nodelist.pop(-1)
        elif len(nodelist) == 2:
            last_one_node = nodelist[-1]
            last_two_node = nodelist[-2]
            last_two_node.next = last_one_node.next
            last_one_node.next = last_two_node
            return last_one_node
        elif len(nodelist) == 3:
            last_one_node = nodelist[-1]
            last_two_node = nodelist[-2]
            last_three_node = nodelist[-3]
            temp = last_one_node.next
            last_three_node.next = last_one_node
            last_one_node.next = last_two_node
            last_two_node.next = temp
            return last_three_node
        elif len(nodelist) == 1:
            return nodelist[0]
    return []


l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
head = swapPairs(l1)
while head:
    print(head.val)
    head = head.next


# 26. 删除有序数组中的重复项
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
def removeDuplicatesDoublePointer(nums: [int]) -> int:
    if not nums:
        return 0
    slowPointer = 1
    fastPointer = 1
    length = len(nums)
    while fastPointer < length:
        if nums[fastPointer] != nums[fastPointer - 1]:
            nums[slowPointer] = nums[fastPointer]
            slowPointer += 1
        fastPointer += 1
    nums = nums[:slowPointer]
    return slowPointer


# 27. 移除元素
# 给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
def removeElement(nums: [int], val: int) -> int:
    if not nums:
        return 0
    length = len(nums)
    slowPointer = 0
    fastPointer = 0
    while fastPointer < length:
        if nums[fastPointer] != val:
            nums[slowPointer] = nums[fastPointer]
            slowPointer += 1
        fastPointer += 1
    nums = nums[:slowPointer]
    return slowPointer
# 31. 下一个排列
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间


def nextPermutation(nums):
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            temp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = temp
            return nums
    nums.sort()
    return nums


nums = [3, 2, 1]
nextPermutation(nums)


# 32. 最长有效括号
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。


def longestValidParentheses(s):
    start = s.index('(')
    left = 0
    counter = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            left += 1
        else:
            left -= 1
            counter += 1
    if left > 0:
        output = counter
    else:
        output = counter - abs(left)
    return 2 * output


s = ")()())"
longestValidParentheses(s)


# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums1，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是O(log n1) 级别。
# 如果数组中不存在目标值，返回[-1, -1]。


def searchRange(nums, target):
    if target in nums:
        start = nums.index(target)
        output = [start]
        while nums[start + 1] == target:
            start += 1
        output.append(start)
        return output
    else:
        return [-1, -1]


nums = [5, 7, 7, 8, 10]
target = 8
searchRange(nums, target)


# 39. 组合总和
# 给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
# candidates中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括target）都是正整数。
# 解集不能包含重复的组合。


def combinationSum(candidates, target):
    candidates.sort()
    output = []
    sub_output = []

    def recursion(num, candidates):
        for i in candidates:
            if num - i > 0:
                sub_output.append(i)
                recursion(num - i, candidates)
                sub_output.pop(-1)
            elif num - i == 0:
                sub_output.append(i)
                output.append(sub_output.copy())
                # append相当于引用，所以需要copy()
                sub_output.pop(-1)
                return
            else:
                return

    recursion(target, candidates)
    result = []
    for i in output:
        i.sort()
        if i not in result:
            result.append(i)
    return result


# 如果list是多维，不能用list(set())去重


candidates = [2, 3, 5]
target = 8
combinationSum(candidates, target)


# 42. 接雨水
# 给定 n1 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


def trap(heights):
    area = []
    if sum(heights) == 0 or sum(heights) == 1:
        return 0
    for i in range(len(heights)):
        if heights[i] != 0:
            heights = heights[i:]
            break
    for i in range(len(heights) - 1, 0, -1):
        if heights[i] != 0:
            heights = heights[:i + 1]
            break

    def edgearea(edge, direction):
        if direction == 'left':
            sub_heights = heights[:edge]
            left_upper = edge - 1
            while sub_heights:
                sub_index = []
                for i in range(0, len(sub_heights)):
                    if sub_heights[i] == max(sub_heights):
                        sub_index.append(i)
                get_area([sub_index[0], left_upper], 'left')
                sub_heights = heights[:sub_index[0]]
                left_upper = sub_index[0] - 1
        if direction == 'right':
            sub_heights = heights[edge + 1:]
            right_lower = edge + 1
            while sub_heights:
                sub_index = []
                for i in range(0, len(sub_heights)):
                    if sub_heights[i] == max(sub_heights):
                        sub_index.append(i + right_lower)
                get_area([right_lower, sub_index[-1]], 'right')
                sub_heights = heights[sub_index[-1] + 1:]
                right_lower = sub_index[-1] + 1

    def get_area(index, pattern):
        if pattern == 'left':
            for i in range(index[0], index[1] + 1):
                area.append(heights[index[0]] - heights[i])
        if pattern == 'right':
            for i in range(index[0], index[1] + 1):
                area.append(heights[index[1]] - heights[i])
        if pattern == 'equal':
            for i in range(index[0], index[1]):
                area.append(heights[index[0]] - heights[i])

    if heights.count(max(heights)) == 1:
        center = heights.index(max(heights))
        edgearea(center, 'left')
        edgearea(center, 'right')
    else:
        index_list = []
        for i in range(0, len(heights)):
            if heights[i] == max(heights):
                index_list.append(i)
        center1 = index_list[0]
        center2 = index_list[-1]
        get_area([center1, center2], 'equal')
        edgearea(center1, 'left')
        edgearea(center2, 'right')
    return sum(area)


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trap(heights)


# 46. 全排列
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。


def permute(nums):
    output = []

    def recursion(num):
        if len(num) == len(nums):
            output.append(num.copy())
            return
        for i in nums:
            if i not in num:
                # num.append(i)
                # recursion(num)
                # 不能实现功能，因为num本身也改变了
                recursion(num + [i])

    # 使用（参数+变量）的方式来传递参数
    recursion([])
    return output


nums = [1, 2, 3]
permute(nums)


# 48. 旋转图像
# 给定一个 n1×n1 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


def rotate(matrix):
    length = len(matrix[0])
    for i in range(int((length + 1) / 2) + 1):
        for j in range(i, length - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[length - 1 - j][i]
            matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
            matrix[j][length - 1 - i] = temp
    return matrix


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
rotate(matrix)


# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。


def groupAnagrams(strs):
    output = []
    history = []
    for i in strs:
        l = list(i)
        l.sort()
        if l not in history:
            history.append(l)
            output.append([])
            output[history.index(l)].append(i)
        else:
            output[history.index(l)].append(i)
    return output


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)


# 50. Pow(x, n1)
# 实现 pow(x, n1) ，即计算 x 的 n1 次幂函数（即，xn）。
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / myPow(x, - n)
    # result = x
    # counter = 1
    # while counter != n1:
    #     if (2 * counter) > n1:
    #         counter = counter + 1
    #         result = result * x
    #     else:
    #         result = result * result
    #         counter = counter * 2
    # return result
    result = 1
    while n != 0:
        if n % 2 == 1:
            result *= x
        n = int(n / 2)
        x *= x
    return result


myPow(2, 10)
