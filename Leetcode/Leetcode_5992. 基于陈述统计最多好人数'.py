"""
5992. 基于陈述统计最多好人数
游戏中存在两种角色：
好人：该角色只说真话。
坏人：该角色可能说真话，也可能说假话。
给你一个下标从 0 开始的二维整数数组 statements ，大小为 n x n ，表示 n 个玩家对彼此角色的陈述。具体来说，statements[i][j] 可以是下述值之一：
0 表示 i 的陈述认为 j 是 坏人 。
1 表示 i 的陈述认为 j 是 好人 。
2 表示 i 没有对 j 作出陈述。
另外，玩家不会对自己进行陈述。形式上，对所有 0 <= i < n ，都有 statements[i][i] = 2 。
根据这 n 个玩家的陈述，返回可以认为是 好人 的 最大 数目。
"""
from typing import List


def maximumGood(statements: List[List[int]]) -> int:
    n = len(statements)

    def check(i):
        counter = 0
        for j, row in enumerate(statements):
            if (i >> j) & 1:
                if any(state < 2 and state != (i >> k) & 1 for k, state in enumerate(row)):
                    return 0
                counter += 1
        return counter
    return max(check(i) for i in range(1, 1 << n))





