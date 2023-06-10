"""
1019. 链表中的下一个更大节点

给定一个长度为 n 的链表 head
对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。
如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。
"""
from libraries.utils import ListNode, generateListNode
from typing import Optional, List


def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    result = []
    stack = []
    index = 0
    while head:
        result.append(0)
        while stack and head.val > stack[-1][0]:
            result[stack[-1][1]] = head.val
            stack.pop(-1)
        stack.append((head.val, index))
        index += 1
        head = head.next
    return result


nextLargerNodes(generateListNode([2,1,5]))
nextLargerNodes(generateListNode([2,7,4,3,5]))
