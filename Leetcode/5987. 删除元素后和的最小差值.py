"""
5987. 删除元素后和的最小差值
给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。
你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。
前面 n 个元素属于第一部分，它们的和记为 sumfirst 。
后面 n 个元素属于第二部分，它们的和记为 sumsecond 。
两部分和的 差值 记为 sumfirst - sumsecond 。
比方说，sumfirst = 3 且 sumsecond = 2 ，它们的差值为 1 。
再比方，sumfirst = 2 且 sumsecond = 3 ，它们的差值为 -1 。
请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。
"""
import heapq
from typing import *


def minimumDifference(nums: List[int]) -> int:
    n = len(nums) // 3
    minPq = nums[len(nums) - n:]
    heapq.heapify(minPq)
    suffixMax = [0] * (len(nums) - n + 1)
    suffixMax[-1] = s = sum(minPq)
    for i in range(len(nums) - n - 1, n - 1, -1):
        s += nums[i] - heapq.heappushpop(minPq, nums[i])
        suffixMax[i] = s
    maxPq = [-value for value in nums[:n]]
    heapq.heapify(maxPq)
    prefixMin = -sum(maxPq)
    result = prefixMin - suffixMax[n]
    for i in range(n, len(nums) - n):
        prefixMin += nums[i] + heapq.heappushpop(maxPq, -nums[i])
        result = min(result, prefixMin - suffixMax[i + 1])
    return result


minimumDifference([16, 46, 43, 41, 42, 14, 36, 49, 50, 28, 38, 25, 17, 5, 18, 11, 14, 21, 23, 39, 23])
