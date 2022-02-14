"""
373. 查找和最小的K对数字
给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。
定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
"""
import heapq
from typing import List


def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    result = []
    pq = [(nums1[0] + nums2[j], 0, j) for j in range(min(k, len(nums2)))]
    while pq and len(result) < k:
        _, i, j = heapq.heappop(pq)
        result.append([nums1[i], nums2[j]])
        if i + 1 < len(nums1):
            heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
    return result

