from libraries.utils import ListNode


# 剑指 Offer 52. 两个链表的第一个公共节点
# 输入两个链表，找出它们的第一个公共节点。
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    list1Set = set()
    while headA:
        list1Set.add(headA)
        headA = headA.next
    while headB:
        if headB in list1Set:
            return headB
        headB = headB.next
    return None
