from libraries import List, ListNode
# 141. 环形链表
# 给定一个链表，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。


def hasCycle(head):
    history = []
    while head:
        if head in history:
            return True
        history.append(head)
        head = head.next
    return False


l1 = ListNode.ListNode(3)
l2 = ListNode.ListNode(2)
l3 = ListNode.ListNode(0)
l4 = ListNode.ListNode(-4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2
hasCycle(l1)
l1 = ListNode.ListNode(-1)
hasCycle(l1)
