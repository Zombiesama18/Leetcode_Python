"""
2233. K 次增加后的最大乘积
给你一个非负整数数组 nums 和一个整数 k 。每次操作，你可以选择 nums 中 任一 元素并将它 增加 1 。
请你返回 至多 k 次操作后，能得到的 nums的 最大乘积 。由于答案可能很大，请你将答案对 109 + 7 取余后返回。
"""
import heapq
from typing import List


def maximumProduct(nums: List[int], k: int) -> int:
    MOD = 10 ** 9 + 7
    heapq.heapify(nums)
    while k > 0:
        minValue = heapq.heappop(nums)
        heapq.heappush(nums, minValue + 1)
        k -= 1
    result = 1
    for num in nums:
        result = (result * num) % MOD
    return result
