from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def generateListNode(nodeValues: List):
    if not nodeValues:
        return None
    l1 = ListNode(nodeValues.pop(0))
    head = l1
    while nodeValues:
        head.next = ListNode(nodeValues.pop(0))
        head = head.next
    return l1


def traverseListNode(head):
    temp = head
    while temp:
        print(temp.val, end='->')
        temp = temp.next


def addUpListNodeByTenForward(head: ListNode):
    temp = head
    number = 0
    while temp:
        number = number * 10 + temp.val
        temp = temp.next
    return number


def addUpListNodeByTenBackward(head: ListNode):
    temp = head
    multiplier = 1
    result = 0
    while temp:
        result = result + temp.val * multiplier
        temp = temp.next
        multiplier = multiplier * 10
    return result


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def generateTreebyLevelOrder(levelOrder):
    length = len(levelOrder)
    nodeList = list()
    for item in levelOrder:
        if item is None:
            nodeList.append(None)
        else:
            nodeList.append(TreeNode(item))
    for i in range(length):
        if 2 * i + 2 > length - 1:
            break
        if nodeList[i]:
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


def preorderTraversal(root):
    result = []

    def subPreorderTraversal(node):
        if not node:
            return
        result.append(node.val)
        subPreorderTraversal(node.left)
        subPreorderTraversal(node.right)
        return

    subPreorderTraversal(root)
    return result


def postorderTraversal(root):
    result = []

    def subPostorderTraversal(node):
        if not node:
            return
        subPostorderTraversal(node.left)
        subPostorderTraversal(node.right)
        result.append(node.val)
        return

    subPostorderTraversal(root)
    return result

