# 802. 找到最终的安全状态
# 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。
# 对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。
# 返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。
# 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，
# 满足 (i, j) 是图的一条有向边。

# 方法：DFS + 三色标记
# 白色（用 00 表示）：该节点尚未被访问；
# 灰色（用 11 表示）：该节点位于递归栈中，或者在某个环上；
# 黑色（用 22 表示）：该节点搜索完毕，是一个安全节点。
def eventualSafeNodes(graph: [[int]]) -> [int]:
    length = len(graph)
    colors = [0] * length

    def dfs(node: int):
        if colors[node] > 0:
            return colors[node] == 2
        colors[node] = 1
        for nextNode in graph[node]:
            if not dfs(nextNode):
                return False
        colors[node] = 2
        return True

    return [i for i in range(length) if dfs(i)]


eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])







