"""
2055. 蜡烛之间的盘子
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，
其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。
同时给你一个下标从 0 开始的二维整数数组 queries ，
其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。
对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。
如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。
比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。
子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。
"""
from typing import List


def platesBetweenCandles(s: str, queries: List[List[int]]) -> List[int]:
    candlesSoFar = [0] * len(s)
    platesSoFar = [0] * len(s)
    lastCandleIndexs = [-1] * len(s)
    nextCandleIndexs = [float('INF')] * len(s)
    lastFlagIndex = 0
    candleCounter, plateCounter = 0, 0
    lastCandleIndex = -1
    for i in range(len(s)):
        if s[i] == '|':
            candleCounter += 1
            lastCandleIndex = i
            for idx in range(lastFlagIndex, i + 1):
                nextCandleIndexs[idx] = i
            lastFlagIndex = i
        else:
            plateCounter += 1
        lastCandleIndexs[i] = lastCandleIndex
        candlesSoFar[i] = candleCounter
        platesSoFar[i] = plateCounter
    result = []
    for start, to in queries:
        if s[start] == s[to] == '|':
            result.append(platesSoFar[to] - platesSoFar[start])
        elif s[start] == '|':
            if lastCandleIndexs[to] == start:
                result.append(0)
            else:
                result.append(platesSoFar[lastCandleIndexs[to]] - platesSoFar[start])
        elif s[to] == '|':
            if nextCandleIndexs[start] == to:
                result.append(0)
            else:
                result.append(platesSoFar[to] - platesSoFar[nextCandleIndexs[start]])
        else:
            if candlesSoFar[to] == candlesSoFar[start]:
                result.append(0)
            else:
                result.append(platesSoFar[lastCandleIndexs[to]] - platesSoFar[nextCandleIndexs[start]])
    return result


platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]])
