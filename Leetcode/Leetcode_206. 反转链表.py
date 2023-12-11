from libraries.utils import ListNode, generateListNode, traverseListNode


# 206. 反转链表
# 反转一个单链表。
def reverseList(head: ListNode):
    nodelist = []
    while head:
        nodelist.append(head)
        head = head.next
    for i in range(len(nodelist) - 1, 0, -1):
        nodelist[i].next = nodelist[i - 1]
    nodelist[0].next = None
    return nodelist[-1]


head = generateListNode([1, 2, 3, 4, 5])
head = reverseList(head)
traverseListNode(head)
