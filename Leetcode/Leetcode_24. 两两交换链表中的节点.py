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
    print('\n')
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


l1 = generateListNode([1, 2, 3, 4])
traverseListNode(l1)
head = swapPairs(l1)
traverseListNode(head)


def swapPairs_v2(head):
    sentinel = ListNode()
    stack = []
    former_node = sentinel
    while head:
        stack.append(head)
        head = head.next
        if len(stack) == 2:
            node2, node1 = stack.pop(), stack.pop()
            former_node.next = node2
            node2.next = node1
            former_node = node1
    if stack:
        former_node.next = stack.pop()
        former_node = former_node.next
    former_node.next = None
    return sentinel.next


swapPairs_v2(generateListNode([1,2,3,4]))
