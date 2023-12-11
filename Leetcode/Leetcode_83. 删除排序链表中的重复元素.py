from libraries.utils import generateListNode, traverseListNode, ListNode


# 83. 删除排序链表中的重复元素
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
# 返回同样按升序排列的结果链表。
def deleteDuplicatesI(head: ListNode):
    if not head:
        return head
    formerNode = head
    currentNode = head.next
    while currentNode:
        if currentNode.val == formerNode.val:
            currentNode = currentNode.next
        else:
            formerNode.next = currentNode
            formerNode = currentNode
            currentNode = currentNode.next
    formerNode.next = None
    return head


head1 = generateListNode([1, 1, 2])
traverseListNode(head1)
head1 = deleteDuplicatesI(head1)
traverseListNode(head1)
head2 = generateListNode([1, 1, 2, 3, 3])
traverseListNode(head2)
head2 = deleteDuplicatesI(head2)
traverseListNode(head2)
