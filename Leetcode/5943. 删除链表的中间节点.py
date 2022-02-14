"""
5943. 删除链表的中间节点
给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。
长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。
对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。
"""
from libraries.utils import ListNode


def deleteMiddle(head):
    counter = 0
    target = head
    current_node = head.next
    while current_node:
        counter += 1
        if counter % 2 == 1:
            former_node = target
            target = target.next
        current_node = current_node.next
    if target == head:
        return None
    former_node.next = target.next
    return head



