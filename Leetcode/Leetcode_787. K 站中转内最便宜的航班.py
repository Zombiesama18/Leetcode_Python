# 787. K 站中转内最便宜的航班
# 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，
# 以价格 pricei 抵达 toi。
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，
# 使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。


# DFS
import collections


def findCheapestPrice(n: int, flights: [[int]], src: int, dst: int, k: int) -> int:
    flightsDict = collections.defaultdict(list)
    for flight in flights:
        flightsDict[flight[0]].append([flight[1], flight[2]])
    minPrice = float('INF')
    traversedSpots = set()

    def DFS(current: int, currentPrice: int, traversedNumber: int):
        nonlocal minPrice
        if traversedNumber > k + 1:
            return
        traversedSpots.add(current)
        if current == dst:
            minPrice = min(minPrice, currentPrice)
        for nextFlight in flightsDict[current]:
            DFS(nextFlight[0], currentPrice + nextFlight[1], traversedNumber + 1)
        return

    DFS(src, 0, 0)
    if dst not in traversedSpots:
        return -1
    else:
        return int(minPrice)


findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)


# 动态规划
def findCheapestPriceByDP(n: int, flights: [[int]], src: int, dst: int, k: int) -> int:
    f = [[float('INF')] * n for _ in range(k + 2)]
    f[0][src] = 0
    for t in range(1, k + 2):
        for j, i, cost in flights:
            f[t][i] = min(f[t][i], f[t - 1][j] + cost)
    result = min(f[t][dst] for t in range(1, k + 2))
    return -1 if result == float('INF') else result
