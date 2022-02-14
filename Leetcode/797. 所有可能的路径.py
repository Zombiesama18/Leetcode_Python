# 797. 所有可能的路径
# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
# 二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。
# 译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。
def allPathsSourceTarget(graph:  [[int]]) -> [[int]]:
    result = []
    length = len(graph)

    def DFS(currentNode: int, path: list):
        nonlocal length
        if currentNode == length - 1:
            result.append(path)
            return
        for nextNode in graph[currentNode]:
            DFS(nextNode, path + [nextNode])

    DFS(0, [0])
    return result


allPathsSourceTarget([[1,2],[3],[3],[]])
allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
allPathsSourceTarget([[1],[]])
allPathsSourceTarget([[1,2,3],[2],[3],[]])
allPathsSourceTarget([[1,3],[2],[3],[]])
