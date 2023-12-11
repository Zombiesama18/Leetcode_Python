"""
5958. 股票平滑下跌阶段的数目
给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。
一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。
请你返回 平滑下降阶段 的数目。
"""
import collections
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        q = collections.deque([(i, i) for i in range(len(prices))])
        result = 0

        def is_valid(start_index, end_index):
            return prices[start_index] - prices[end_index] == end_index - start_index

        while q:
            start, end = q.popleft()
            if is_valid(start, end):
                result += 1
                if end + 1 < len(prices):
                    q.append((start, end + 1))
        return result

    def getDescentPeriodsVersion2(self, prices: List[int]) -> int:
        dp = [1 for _ in range(len(prices))]
        result = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp[i] += dp[i - 1]
            result += dp[i]
        return result
