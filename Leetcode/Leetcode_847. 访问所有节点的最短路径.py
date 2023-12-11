# 847. 访问所有节点的最短路径
# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
import collections


def shortestPathLength(graph: [[int]]) -> int:
    length = len(graph)
    presentationOfAllCovered = 2 ** length - 1
    nodeQueue = collections.deque((x, 1 << x) for x in range(length))
    edgeDict = collections.defaultdict(lambda : length * length)
    for x in range(length):
        edgeDict[x, 1 << x] = 0
    while nodeQueue:
        currentNode, coveredNode = nodeQueue.popleft()
        currentEdgeNumber = edgeDict[currentNode, coveredNode]
        if coveredNode == presentationOfAllCovered:
            return currentEdgeNumber
        for nextNode in graph[currentNode]:
            tempCoveredNode = coveredNode | (1 << nextNode)
            if currentEdgeNumber < edgeDict[nextNode, tempCoveredNode]:
                edgeDict[nextNode, tempCoveredNode] = currentEdgeNumber + 1
                nodeQueue.append((nextNode, tempCoveredNode))


shortestPathLength([[1,2,3],[0],[0],[0]])

