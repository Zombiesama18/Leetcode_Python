"""
2208. 将数组和减半的最少操作次数
给你一个正整数数组 nums 。每一次操作中，你可以从 nums 中选择 任意 一个数并将它减小到 恰好 一半。
（注意，在后续操作中你可以对减半过的数继续执行操作）
请你返回将 nums 数组和 至少 减少一半的 最少 操作数。
"""
import heapq
from typing import List


def halveArray(nums: List[int]) -> int:
    summation = sum(nums)
    priorityQueue = [- num for num in nums]
    heapq.heapify(priorityQueue)
    target = summation / 2
    counter = 0
    process = 0
    while process < target:
        maxNumber = - heapq.heappop(priorityQueue)
        halvedNumber = maxNumber / 2
        counter += 1
        process += halvedNumber
        heapq.heappush(priorityQueue, - halvedNumber)
    return counter

