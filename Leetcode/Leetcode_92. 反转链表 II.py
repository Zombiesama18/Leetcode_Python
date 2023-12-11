class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 工具方法
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


# 92. 反转链表 II
# 反转从位置 m 到 n1 的链表。请使用一趟扫描完成反转。
def reverseBetween(head: ListNode, left: int, right: int):
    if left < 1 or right <= left or not head:
        return head
    i = 0
    sentinel = ListNode(0)
    sentinel.next = head
    node = sentinel
    stack = list()
    while i < left - 1:
        node = node.next
        i += 1
    leftStart = node
    while i < right:
        node = node.next
        stack.append(node)
        i += 1
    rightEnd = node.next
    while stack:
        leftStart.next = stack.pop()
        leftStart = leftStart.next
    leftStart.next = rightEnd
    return sentinel.next
