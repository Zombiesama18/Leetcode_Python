"""
143. 重排链表

给定一个单链表 L 的头节点 head ，单链表 L 表示为：
L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from typing import Optional
import collections
from libraries.utils import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        sentinel = ListNode()
        sentinel.next = head
        while head:
            nodes.append(head)
            head = head.next
        pointer = sentinel
        for i in range(len(nodes) // 2):
            pointer.next = nodes[i]
            pointer = pointer.next
            pointer.next = nodes[len(nodes) - i - 1]
            pointer = pointer.next
        if len(nodes) % 2 != 0:
            pointer.next = nodes[len(nodes) // 2]
        head = sentinel.next

