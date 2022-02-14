# 725. 分隔链表
# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
# 返回一个符合上述规则的链表的列表。
# 举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
from libraries.utils import ListNode


def splitListToParts(head: ListNode, k: int) -> [ListNode]:
    nodeList = []
    while head:
        nodeList.append(head)
        head = head.next
    length = len(nodeList)
    subLength = length // k
    extraLength = length % k
    result = [None for _ in range(k)]
    counter = 0
    for i in range(k):
        if counter >= length:
            break
        if extraLength > 0:
            nodeList[counter + subLength].next = None
            result[i] = nodeList[counter]
            counter += subLength + 1
            extraLength -= 1
        else:
            nodeList[counter + subLength - 1].next = None
            result[i] = nodeList[counter]
            counter += subLength
    return result





