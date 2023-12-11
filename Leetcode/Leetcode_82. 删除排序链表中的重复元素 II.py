class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 工具方法
def generateListNode(nodeValues: list):
    l1 = ListNode(nodeValues.pop(0))
    head = l1
    while nodeValues:
        head.next = ListNode(nodeValues.pop(0))
        head = head.next
    return l1


def traverseListNode(head):
    while head:
        print(head.val, end='->')
        head = head.next


# 82. 删除排序链表中的重复元素 II
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。
# 返回同样按升序排列的结果链表。
def deleteDuplicates(head: ListNode):
    if not head:
        return head
    sentinel = ListNode(0, head)
    isDuplicate = False
    formerNode = sentinel
    currentNode = head
    while currentNode.next:
        if currentNode.val == currentNode.next.val:
            currentNode = currentNode.next
            isDuplicate = True
        else:
            if isDuplicate:
                isDuplicate = False
            else:
                formerNode.next = currentNode
                formerNode = currentNode
            currentNode = currentNode.next
    if isDuplicate:
        formerNode.next = None
    else:
        formerNode.next = currentNode
    return sentinel.next


head1 = generateListNode([1, 1, 1, 2, 3])
traverseListNode(head1)
head1 = deleteDuplicates(head1)
traverseListNode(head1)
head2 = generateListNode([1, 2, 3, 3, 4, 4, 5])
traverseListNode(head2)
head2 = deleteDuplicates(head2)
traverseListNode(head2)

