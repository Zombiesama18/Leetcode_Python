# 5915. 找出临界点之间的最小和最大距离
# 链表中的 临界点 定义为一个 局部极大值点 或 局部极小值点 。
# 如果当前节点的值 严格大于 前一个节点和后一个节点，那么这个节点就是一个  局部极大值点 。
# 如果当前节点的值 严格小于 前一个节点和后一个节点，那么这个节点就是一个  局部极小值点 。
# 注意：节点只有在同时存在前一个节点和后一个节点的情况下，才能成为一个 局部极大值点 / 极小值点 。
# 给你一个链表 head ，返回一个长度为 2 的数组 [minDistance, maxDistance] ，其中 minDistance 是任意两个不同临界点之间的最小距离，
# maxDistance 是任意两个不同临界点之间的最大距离。如果临界点少于两个，则返回 [-1，-1] 。
from libraries.utils import ListNode


def nodesBetweenCriticalPoints(head: [ListNode]) -> [int]:
    minDistance, maxDistance = float('INF'), float('-INF')
    criticalPointIndex = []
    lastNumber = head.val
    head = head.next
    index = 0
    while head.next:
        if lastNumber < head.val > head.next.val or lastNumber > head.val < head.next.val:
            criticalPointIndex.append(index)
            if len(criticalPointIndex) > 1:
                minDistance = min(minDistance, index - criticalPointIndex[-2])
                maxDistance = max(maxDistance, index - criticalPointIndex[0])
        lastNumber = head.val
        head = head.next
        index += 1
    if minDistance == float('INF'):
        return [-1, -1]
    return [minDistance, maxDistance]



