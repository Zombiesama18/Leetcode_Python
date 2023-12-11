from libraries.utils import ListNode, generateListNode, addUpListNodeByTenForward, addUpListNodeByTenBackward


# 2. 两数相加
# 给出两个非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0开头。


def addTwoNumbersStepByStep(l1: ListNode, l2: ListNode):
    nodeList1 = []
    nodeList2 = []
    while l1:
        nodeList1.append(l1.val)
        l1 = l1.next
    while l2:
        nodeList2.append(l2.val)
        l2 = l2.next
    carryBit = False
    resultList = []
    if len(nodeList1) < len(nodeList2):
        temp = nodeList1
        nodeList1 = nodeList2
        nodeList2 = temp
    nodeList2 = nodeList2 + [0] * (len(nodeList1) - len(nodeList2))
    while nodeList2:
        tempCalculate = nodeList1.pop(0) + nodeList2.pop(0) + carryBit
        resultList.append(tempCalculate % 10)
        if carryBit:
            carryBit = False
        if tempCalculate >= 10:
            carryBit = True
    if carryBit:
        resultList.append(1)
    headNode = ListNode(resultList[0])
    predNode = headNode
    for i in range(1, len(resultList)):
        predNode.next = ListNode(resultList[i])
        predNode = predNode.next
    return headNode


lists1 = [generateListNode([2, 4, 3]), generateListNode([0]), generateListNode([9, 9, 9, 9, 9, 9, 9])]
lists2 = [generateListNode([5, 6, 4]), generateListNode([0]), generateListNode([9, 9, 9, 9])]
for i in range(len(lists1)):
    print('输入：', addUpListNodeByTenForward(lists1[i]), ' + ', addUpListNodeByTenForward(lists2[i]), '\t结果：',
          addUpListNodeByTenForward(addTwoNumbersStepByStep(lists1[i], lists2[i])))


def addTwoNumbersIntegreted(l1: ListNode, l2: ListNode):
    root = ListNode(0)
    currentNode = root
    carryBit = 0
    while l1 or l2 or carryBit:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        addResult = l1Val + l2Val + carryBit
        carryBit = addResult // 10
        currentNode.next = ListNode(addResult % 10)
        currentNode = currentNode.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return root.next


lists1 = [generateListNode([2, 4, 3]), generateListNode([0]), generateListNode([9, 9, 9, 9, 9, 9, 9])]
lists2 = [generateListNode([5, 6, 4]), generateListNode([0]), generateListNode([9, 9, 9, 9])]
for i in range(len(lists1)):
    print('输入：', addUpListNodeByTenForward(lists1[i]), ' + ', addUpListNodeByTenForward(lists2[i]), '\t结果：',
          addUpListNodeByTenForward(addTwoNumbersIntegreted(lists1[i], lists2[i])))
