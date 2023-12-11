"""
1171. 从链表中删去总和值为零的连续节点
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
删除完毕后，请你返回最终结果链表的头节点。
你可以返回任何满足题目要求的答案。
（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
"""
import collections
from typing import Optional

from libraries.utils import ListNode, generateListNode


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        position_dict = collections.defaultdict(list)
        position_dict[0] = sentinel
        temp_sum = 0
        while head:
            temp_sum += head.val
            position_dict[temp_sum] = head
            head = head.next
        temp_sum = 0
        head = sentinel
        while head:
            temp_sum += head.val
            head.next = position_dict[temp_sum].next
            head = head.next
        return sentinel.next


Solution().removeZeroSumSublists(generateListNode([1,3,2,-3,-2,5,5,-5,1]))
