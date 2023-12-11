from libraries.utils import ListNode, generateListNode, traverseListNode


# 19. 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n1 个节点，并且返回链表的头结点。
def removeNthFromEnd(head: ListNode, n: int):
    nodelist = [ListNode(0)]
    nodelist[0].next = head
    while head:
        nodelist.append(head)
        head = head.next
    nodelist[- n - 1].next = nodelist[- n].next
    return nodelist[0].next


heads = list(map(generateListNode, [[1,2,3,4,5], [1], [1,2]]))
ns = [2, 1, 1]
for i in range(len(heads)):
    print('输入：', end='\t')
    traverseListNode(heads[i])
    print('和', ns[i], '\t结果：', end='\t')
    traverseListNode(removeNthFromEnd(heads[i], ns[i]))
    print()
