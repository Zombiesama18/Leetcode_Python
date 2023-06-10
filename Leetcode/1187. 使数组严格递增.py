"""
1187. 使数组严格递增

给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length
和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
如果无法让 arr1 严格递增，请返回 -1。
"""
import bisect
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0
        arr2 = list(sorted(set(arr2)))
        dp = [[float('inf')] * (min(len(arr1), len(arr2)) + 1) for _ in range(len(arr1) + 1)]
        dp[0][0] = -1
        for i in range(1, len(arr1) + 1):
            for j in range(min(i, len(arr2)) + 1):
                if arr1[i - 1] > dp[i - 1][j]:
                    dp[i][j] = arr1[i - 1]
                if j != 0 and dp[i - 1][j - 1] != float('inf'):
                    if (k := bisect.bisect_right(arr2, dp[i - 1][j - 1], j - 1)) < len(arr2):
                        dp[i][j] = min(dp[i][j], arr2[k])
                if i == len(arr1) and dp[i][j] != float('inf'):
                    return j
        return -1


Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])
Solution().makeArrayIncreasing([0,11,6,1,4,3], [5,4,11,10,1,0])
