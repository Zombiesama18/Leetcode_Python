# 815. 公交路线（需要学习更快方法）
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
from collections import deque


def numBusesToDestinationSlowVersion(routes: [[int]], source: int, target: int) -> int:
    if source == target:
        return 0
    hashRoutes = []
    hashRoutes.extend(set(item) for item in routes)
    length = len(hashRoutes)

    def getNext(stop: int, step: int):
        for i in range(length):
            if stop in hashRoutes[i]:
                temp = list(hashRoutes[i])
                for j in range(len(temp)):
                    if temp[j] not in traversedStop:
                        q.append((nextStop, step + 1))
                        traversedStop.add(nextStop)
                        yield temp[j]

    q = deque([(source, 0)])
    traversedStop = {source}
    while q:
        currentStop, step = q.popleft()
        for nextStop in getNext(currentStop, step):
            if nextStop == target:
                return step + 1
    return -1


def numBusesToDestination(routes: [[int]], source: int, target: int) -> int:
    if source == target:
        return 0
    busGraph = dict()
    hashRoutes = []
    hashRoutes.extend(set(item) for item in routes)
    length = len(hashRoutes)
    for i in range(length):
        busGraph[i] = list()
    for i in range(length - 1):
        for j in range(i + 1, length):
            for k in hashRoutes[i]:
                if k in hashRoutes[j]:
                    busGraph[i].append(j)
                    busGraph[j].append(i)
                    break

    q = deque()
    traversedBus = set()
    for i in range(length):
        if source in hashRoutes[i]:
            q.append((i, 1))
            traversedBus.add(i)
    while q:
        currentBus, step = q.popleft()
        if target in hashRoutes[currentBus]:
            return step
        for nextBus in busGraph[currentBus]:
            if nextBus not in traversedBus:
                q.append((nextBus, step + 1))
                traversedBus.add(nextBus)
    return -1


numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)
numBusesToDestination(
    [[1, 9, 12, 20, 23, 24, 35, 38], [10, 21, 24, 31, 32, 34, 37, 38, 43], [10, 19, 28, 37], [8], [14, 19],
     [11, 17, 23, 31, 41, 43, 44], [21, 26, 29, 33], [5, 11, 33, 41], [4, 5, 8, 9, 24, 44]], 37, 28)
