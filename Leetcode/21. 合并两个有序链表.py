from libraries.utils import ListNode, generateListNode, traverseListNode
# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


def mergeTwoLists(l1: ListNode, l2: ListNode):
    if not l1:
        return l2
    if not l2:
        return l1
    sentinel = ListNode('0')
    currentNode = sentinel
    while l1 or l2:
        if not l1:
            currentNode.next = l2
            l2 = l2.next
        elif not l2:
            currentNode.next = l1
            l1 = l1.next
        elif l1.val < l2.val:
            currentNode.next = l1
            l1 = l1.next
        else:
            currentNode.next = l2
            l2 = l2.next
        currentNode = currentNode.next
    return sentinel.next


nodes1 = [generateListNode([1, 2, 4]), generateListNode([]), generateListNode([])]
nodes2 = [generateListNode([1, 3, 4]), generateListNode([]), generateListNode([0])]
for i in range(len(nodes1)):
    print('输入：', end='')
    traverseListNode(nodes1[i])
    print('\t和：', end='')
    traverseListNode(nodes2[i])
    print('结果：', end='')
    traverseListNode(mergeTwoLists(nodes1[i], nodes2[i]))
    print(end='\n')
