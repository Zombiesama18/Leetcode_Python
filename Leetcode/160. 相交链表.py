from libraries.utils import generateListNode, ListNode


# 160. 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。
def getIntersectionNode(headA, headB):
    nodeOfHeadA, nodeOfHeadB = [], []
    while headA:
        nodeOfHeadA.append(headA)
        headA = headA.next
    while headB:
        nodeOfHeadB.append(headB)
        headB = headB.next
    prevNode = None
    while nodeOfHeadA and nodeOfHeadB:
        currentNode = nodeOfHeadA.pop(-1)
        if currentNode == nodeOfHeadB.pop(-1):
            prevNode = currentNode
        else:
            return prevNode
    return prevNode





l1 = ListNode(4)
l2 = ListNode(1)
l3 = ListNode(5)
l4 = ListNode(0)
l5 = ListNode(1)
l6 = ListNode(8)
l7 = ListNode(4)
l8 = ListNode(5)
l1.next = l2
l2.next = l6
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
getIntersectionNode(l1, l3)
l1 = ListNode(0)
l2 = ListNode(9)
l3 = ListNode(1)
l4 = ListNode(3)
l5 = ListNode(2)
l6 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l5
l4.next = l5
l5.next = l6
getIntersectionNode(l1, l4)
l1 = ListNode(0)
l2 = ListNode(9)
l3 = ListNode(1)
l4 = ListNode(3)
l5 = ListNode(2)
l1.next = l2
l2.next = l3
l4.next = l5
getIntersectionNode(l1, l4)