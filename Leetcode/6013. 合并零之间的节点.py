"""
6013. 合并零之间的节点
给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 Node.val == 0 。
对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 0 移除，修改后的链表不应该含有任何 0 。
 返回修改后链表的头节点 head 。
"""
from typing import *
from libraries.utils import ListNode


def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode()
    head = head.next
    temp = 0
    tempNode = sentinel
    while head:
        if head.val == 0:
            tempNode.next = ListNode(val=temp)
            tempNode = tempNode.next
            temp = 0
        else:
            temp += head.val
        head = head.next
    return sentinel.next




