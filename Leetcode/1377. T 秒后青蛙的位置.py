"""
1377. T 秒后青蛙的位置

给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：
在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
青蛙无法跳回已经访问过的顶点。
如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
无向树的边用数组 edges 描述，其中 edges[i] = [ai, bi] 意味着存在一条直接连通 ai 和 bi 两个顶点的边。
返回青蛙在 t 秒后位于目标顶点 target 上的概率。与实际答案相差不超过 10-5 的结果将被视为正确答案。
"""
import collections
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        edges_dict = collections.defaultdict(list)
        for start, end in edges:
            edges_dict[start].append(end)
            edges_dict[end].append(start)
        result = 0
        q = collections.deque([(1, {1}, 0, 1.)])
        while q:
            current_node, history, time_cost, prob = q.popleft()
            if current_node == target and (time_cost == t or len(edges_dict[current_node]) == 0
                                           or (len(edges_dict[current_node]) == 1 and edges_dict[current_node][0]
                                               in history)):
                result += prob
            elif time_cost != t and current_node != target:
                for next_node in edges_dict[current_node]:
                    if next_node not in history:
                        history.add(next_node)
                        q.append((next_node, history.copy(), time_cost + 1, prob *
                                  (1 / (len(set(edges_dict[current_node]).difference(history)) + 1))))
                        history.remove(next_node)
        return result


Solution().frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4)

