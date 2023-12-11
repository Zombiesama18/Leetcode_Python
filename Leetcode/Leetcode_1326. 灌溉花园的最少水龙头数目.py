"""
1326. 灌溉花园的最少水龙头数目
在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。
花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。
给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，
可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。
请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。
"""
from typing import List


def minTaps(n: int, ranges: List[int]) -> int:
    intervals = []
    for i, v in enumerate(ranges):
        intervals.append((max(0, i - v), min(n, i + v)))
    intervals.sort()

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for start, end in intervals:
        if dp[start] == -1:
            return -1
        for i in range(start, end + 1):
            dp[i] = min(dp[i], 1 + dp[start])
    return -1 if dp[-1] == float('inf') else dp[-1]


minTaps(n = 5, ranges = [3,4,1,1,0,0])

