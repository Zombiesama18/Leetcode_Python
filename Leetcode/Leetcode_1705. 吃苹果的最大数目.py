"""
1705. 吃苹果的最大数目
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，
这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，
此时用 apples[i] == 0 且 days[i] == 0 表示。
你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。
给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。
"""
import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        result = 0
        currentDay = 0
        pq = []
        while currentDay < len(apples):
            while pq and pq[0][0] <= currentDay:
                heapq.heappop(pq)
            if apples[currentDay] != 0:
                heapq.heappush(pq, [currentDay + days[currentDay], apples[currentDay]])
            if pq:
                pq[0][1] -= 1
                if pq[0][1] == 0:
                    heapq.heappop(pq)
                result += 1
            currentDay += 1
        while pq:
            while pq and pq[0][0] <= currentDay:
                heapq.heappop(pq)
            if len(pq) == 0:
                break
            p = heapq.heappop(pq)
            result += min(p[0] - currentDay, p[1])
            currentDay += min(p[0] - currentDay, p[1])
        return result





