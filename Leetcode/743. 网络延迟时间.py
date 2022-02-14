# 743. 网络延迟时间
# 有 n 个网络节点，标记为 1 到 n。
# 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
# 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
def networkDelayTime(times: [[int]], n: int, k: int) -> int:
    traversedNode = set()
    nodeDict = {}
    maxCost = 0
    for time in times:
        nodeDict.setdefault(time[0], {})[time[1]] = time[2]

    def dfs(node: int, currentCost: int):
        nonlocal maxCost
        if node in traversedNode:
            return
        traversedNode.add(node)
        maxCost = max(maxCost, currentCost)
        if node not in nodeDict:
            return
        for nextNode, cost in nodeDict[node].items():
            dfs(nextNode, currentCost + cost)

    dfs(k, 0)
    if len(traversedNode) != n:
        return -1
    return maxCost


networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
networkDelayTime([[1,2,1],[2,1,3]], 2, 2)
