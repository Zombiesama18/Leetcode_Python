import collections
import math


def shudu(matrix, partitions):
    candidates = ['1', '2', '3']
    rowSets, colSets = [set() for _ in range(3)], [set() for _ in range(3)]
    partitionSet = [set() for _ in range(3)]
    unfilled = []
    resultCounter = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '*':
                unfilled.append((i, j))
            else:
                if matrix[i][j] in rowSets[i] or matrix[i][j] in colSets[j]:
                    return 'No'
                rowSets[i].add(matrix[i][j])
                colSets[j].add(matrix[i][j])
                partitionSet[int(partitions[i][j][0])].add(matrix[i][j])

    def search(currentIndex):
        nonlocal resultCounter
        if currentIndex == len(unfilled):
            resultCounter += 1
            return
        currentX, currentY = unfilled[currentIndex]
        for candidate in candidates:
            if candidate not in rowSets[currentX] and candidate not in colSets[currentY] \
                    and candidate not in partitionSet[int(partitions[currentX][currentY][0])]:
                rowSets[currentX].add(candidate)
                colSets[currentY].add(candidate)
                partitionSet[int(partitions[currentX][currentY][0])].add(candidate)
                search(currentIndex + 1)
                rowSets[currentX].remove(candidate)
                colSets[currentY].remove(candidate)
                partitionSet[int(partitions[currentX][currentY][0])].remove(candidate)
        return

    search(0)
    if resultCounter == 0:
        return 'No'
    if resultCounter == 1:
        return 'Unique'
    return 'Multiple'


matrix = [['*', '*', '3'], ['*', '*', '*'], ['*', '*', '*']]
partitions = [['00', '10', '11'], ['01', '02', '12'], ['20', '21', '22']]
matrix = [['*', '*', '3'], ['1', '*', '*'], ['*', '*', '2']]
shudu(matrix, partitions)


def eliminateEnemy(n, m, a, b, abilities, matrix):
    def bfs(currentX, currentY, friendIdentifier):
        dq = collections.deque([(currentX, currentY, 0)])
        visited = set()
        while dq:
            x, y, step = dq.popleft()
            for stepX, stepY in directions:
                nextX, nextY = x + stepX, y + stepY
                if 0 <= nextX < n and 0 <= nextY < m and (nextX, nextY) not in visited and matrix[nextX][nextY] != 'w':
                    visited.add((nextX, nextY))
                    if matrix[nextX][nextY] == 'E':
                        shortestDistance[friendIdentifier][indexToPositionEnemy[(nextX, nextY)]] = step + 1
                    else:
                        dq.append((nextX, nextY, step + 1))

    def dfs(friendIndex, friendVisited, enemyVisited, totalDistance):
        if len(enemyVisited) == b:
            nonlocal result
            result = min(result, totalDistance)
            return
        if friendIndex in friendVisited:
            return
        for i in range(b):
            if shortestDistance[friendIndex][i] == -1 or i in enemyVisited:
                continue
            enemyVisited.add(i)
            dfs((friendIndex + 1) % a, friendVisited, enemyVisited, totalDistance + shortestDistance[friendIndex][i])
            enemyVisited.remove(i)

    enemyCounter = 0
    indexToPositionEnemy, indexToPosition = {}, {}
    shortestDistance = [[-1 for _ in range(b)] for _ in range(a)]
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'E':
                indexToPositionEnemy[(i, j)] = enemyCounter
                enemyCounter += 1
            if matrix[i][j].isdigit():
                indexToPosition[int(matrix[i][j])] = (i, j)
    for i in range(a):
        bfs(indexToPosition[i][0], indexToPosition[i][1], i)
    result = float('INF')
    for i in range(a):
        dfs(i, {i}, set(), 0)
    return result if result != float('INF') else -1









