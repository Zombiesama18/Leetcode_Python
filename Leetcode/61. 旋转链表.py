from libraries import List, ListNode


# 61. 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
def rotateRight(head: ListNode, k: int):
    if not head or k == 0:
        return head
    nodeStack = list()
    while head:
        nodeStack.append(head)
        head = head.next
    index = k % len(nodeStack)
    head = nodeStack[-index]
    nodeStack[-1].next = nodeStack[0]
    nodeStack[-index - 1].next = None
    return head


list1 = List.List([1, 2, 3, 4, 5])
list1.traverseListNode()
list1.head = rotateRight(list1.head, 2)
list1.traverseListNode()
list2 = List.List([0, 1, 2])
list2.traverseListNode()
list2.head = rotateRight(list2.head, 4)
list2.traverseListNode()
list3 = List.List([1])
list3.traverseListNode()
list3.head = rotateRight(list3.head, 1)
list3.traverseListNode()
