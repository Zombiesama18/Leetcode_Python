"""
1043. 分隔数组以得到最大和

给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分隔完成后，
每个子数组的中的所有值都会变为该子数组中的最大值。
返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。
"""
from typing import List
import heapq


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            max_value = 0
            for j in range(k):
                if i + j == len(arr):
                    break
                if arr[i + j] > max_value:
                    max_value = arr[i + j]
                dp[i + j + 1] = max(dp[i + j + 1], dp[i] + max_value * (j + 1))
        return dp[-1]


Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)
