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
