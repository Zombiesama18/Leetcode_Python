from libraries.utils import ListNode, generateListNode, traverseListNode


# 23. 合并K个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
def mergeKListsByFlattening(lists: [ListNode]):
    nodelist = []
    for i in lists:
        while i:
            nodelist.append(i)
            i = i.next

    def getval(node):
        return node.val

    nodelist.sort(key=getval)
    for i in range(len(nodelist) - 1):
        nodelist[i].next = nodelist[i + 1]
    if nodelist:
        return nodelist[0]
    else:
        return None


nodeList = [[generateListNode([1, 4, 5]), generateListNode([1, 3, 4]), generateListNode([2, 6])], [], [[]]]
for node in nodeList:
    print('input: ', end='')
    for n in node:
        traverseListNode(n)
        print(end='\t')
    print(end='\n')
    print('output: ', end='')
    traverseListNode(mergeKListsByFlattening(node))
    print(end='\n')


def mergeKListsByCombiningButOverTime(lists: [ListNode]):
    if not lists:
        return None
    sentinel = ListNode('0')
    currentNode = sentinel
    flag = bool(max(lists, key=lambda x: x is not None))
    while flag:
        minIndex = min(enumerate(lists), key=lambda x: x[1].val if x[1] else float('INF'))[0]
        currentNode.next = lists[minIndex]
        currentNode = currentNode.next
        lists[minIndex] = lists[minIndex].next
        flag = bool(max(lists, key=lambda x: x is not None))
    return sentinel.next


nodeList = [[generateListNode([]), generateListNode([-2]), generateListNode([-3, -2, 1])],
            [generateListNode([1, 4, 5]), generateListNode([1, 3, 4]), generateListNode([2, 6])], [], [[]]]
for node in nodeList:
    print('input: ', end='')
    for n in node:
        traverseListNode(n)
        print(end='\t')
    print(end='\n')
    print('output: ', end='')
    traverseListNode(mergeKListsByCombiningButOverTime(node))
    print(end='\n')
