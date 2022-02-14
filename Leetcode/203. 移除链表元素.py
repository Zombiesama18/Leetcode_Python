# encoding = utf-8
from libraries.utils import ListNode, generateListNode, traverseListNode


# 203. 移除链表元素
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
def removeElements(head: ListNode, val: int) -> ListNode:
    sentinel = ListNode()
    predecessor = sentinel
    while head:
        if head.val != val:
            predecessor.next = head
            predecessor = predecessor.next
        head = head.next
    predecessor.next = None
    return sentinel.next


head1 = generateListNode([1,2,6,3,4,5,6])
traverseListNode(removeElements(generateListNode([1,2,6,3,4,5,6]), 6))
