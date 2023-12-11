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