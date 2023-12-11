# 407. 接雨水 II
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
import heapq


def trapRainWater(heightMap: [[int]]) -> int:
    if len(heightMap) < 3 or len(heightMap[0]) < 3:
        return 0
    m, n = len(heightMap), len(heightMap[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    pq = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                visited[i][j] = 1
                heapq.heappush(pq, (heightMap[i][j], i * n + j))
    result = 0
    directions = [-1, 0, 1, 0, -1]
    while pq:
        height, position = heapq.heappop(pq)
        for k in range(4):
            nextX, nextY = position // n + directions[k], position % n + directions[k + 1]
            if 0 <= nextX < m and 0 <= nextY < n and visited[nextX][nextY] == 0:
                if height > heightMap[nextX][nextY]:
                    result += height - heightMap[nextX][nextY]
                visited[nextX][nextY] = 1
                heapq.heappush(pq, (max(height, heightMap[nextX][nextY]), nextX * n + nextY))
    return result


