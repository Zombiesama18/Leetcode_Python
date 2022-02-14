from libraries.ListNode import ListNode
# 142. 环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 说明：不允许修改给定的链表。


def detectCycle(head):
    nodelist = []
    while head:
        if head in nodelist:
            return 'tail connects to node index ' + str(nodelist.index(head))
        nodelist.append(head)
        head = head.next
    return 'no cycle'


l4 = ListNode(-4)
l3 = ListNode(0, l4)
l2 = ListNode(2, l3)
l1 = ListNode(3, l2)
l4.next = l2
detectCycle(l1)
l1 = ListNode(1)
detectCycle(l1)
