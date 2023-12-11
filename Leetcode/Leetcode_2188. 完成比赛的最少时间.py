"""
2188. 完成比赛的最少时间
给你一个下标从 0 开始的二维整数数组 tires ，其中 tires[i] = [fi, ri] 表示第 i 种轮胎如果连续使用，第 x 圈需要耗时 fi * ri(x-1) 秒。
比方说，如果 fi = 3 且 ri = 2 ，且一直使用这种类型的同一条轮胎，那么该轮胎完成第 1 圈赛道耗时 3 秒，完成第 2 圈耗时 3 * 2 = 6 秒，
完成第 3 圈耗时 3 * 22 = 12 秒，依次类推。
同时给你一个整数 changeTime 和一个整数 numLaps 。
比赛总共包含 numLaps 圈，你可以选择 任意 一种轮胎开始比赛。每一种轮胎都有 无数条 。每一圈后，
你可以选择耗费 changeTime 秒 换成 任意一种轮胎（也可以换成当前种类的新轮胎）。
请你返回完成比赛需要耗费的 最少 时间。
"""
from typing import *


def minimumFinishTime(tires: List[List[int]], changeTime: int, numLaps: int) -> int:
    min_sec = [float('INF')] * 18
    for f, r in tires:
        x, time, summation = 1, f, 0
        while time <= changeTime + f:
            summation += time
            time *= r
            min_sec[x] = min(min_sec[x], summation)
            x += 1
    dp = [float('INF')] * (numLaps + 1)
    dp[0] = -changeTime
    for i in range(1, numLaps + 1):
        for j in range(1, min(18, i + 1)):
            dp[i] = min(changeTime + dp[i - j] + min_sec[j], dp[i])
    return dp[numLaps]
