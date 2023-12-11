"""
2865. 美丽塔 I

给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。
你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。
如果以下条件满足，我们称这些塔是 美丽 的：
1 <= heights[i] <= maxHeights[i]
heights 是一个 山状 数组。
如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山状 数组：
对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
请你返回满足 美丽塔 要求的方案中，高度和的最大值 。
"""
from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        result = 0
        for start_indices in range(len(maxHeights)):
            last_height = maxHeights[start_indices]
            temp = maxHeights[start_indices]
            for i in range(start_indices - 1, -1, -1):
                temp += min(last_height, maxHeights[i])
                last_height = min(last_height, maxHeights[i])
            last_height = maxHeights[start_indices]
            for i in range(start_indices + 1, len(maxHeights)):
                temp += min(last_height, maxHeights[i])
                last_height = min(last_height, maxHeights[i])
            result = max(result, temp)
        return result

    def maximumSumOfHeights_v2(self, maxHeights: List[int]) -> int:
        result = maxHeights[0]
        prefix, suffix = [], []
        stack = [(-1, -1)]
        temp = 0
        for i, height in enumerate(maxHeights):
            while stack[-1][0] > height:
                last_height, last_index = stack.pop(-1)
                temp -= last_height * (last_index - stack[-1][1])
            temp += height * (i - stack[-1][-1])
            stack.append((height, i))
            prefix.append(temp)
        stack = [(-1, len(maxHeights))]
        temp = 0
        for i in range(len(maxHeights) - 1, 0, -1):
            while stack[-1][0] > maxHeights[i]:
                last_height, last_index = stack.pop(-1)
                temp -= last_height * (stack[-1][1] - last_index)
            temp += maxHeights[i] * (stack[-1][1] - i)
            stack.append((maxHeights[i], i))
            result = max(result, temp + prefix[i - 1])
        return result


Solution().maximumSumOfHeights_v2(maxHeights =[5,3,4,1,1])
