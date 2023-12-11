"""
5955. 摘水果
在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 fruits ，
其中 fruits[i] = [positioni, amounti] 表示共有 amounti 个水果放置在 positioni 上。
fruits 已经按 positioni 升序排列 ，每个 positioni 互不相同 。
另给你两个整数 startPos 和 k 。最初，你位于 startPos 。从任何位置，你可以选择 向左或者向右 走。
在 x 轴上每移动 一个单位 ，就记作 一步 。你总共可以走 最多 k 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。
返回你可以摘到水果的 最大总数 。
"""
import bisect
import collections


def maxTotalFruits(fruits: [[int]], startPos: int, k: int) -> int:
    q = collections.deque([])
    result, length, position = 0, len(fruits), 0
    while position < length and fruits[position][0] <= startPos:
        if abs(fruits[position][0] - startPos) <= k:
            result += fruits[position][1]
            q.append((fruits[position][0], fruits[position][1]))
        position += 1
    temp = result
    while position < length and fruits[position][0] - startPos <= k:
        while q and q[0][0] < startPos and \
                fruits[position][0] - q[0][0] + min(startPos - q[0][0], fruits[position][0] - startPos) > k:
            temp -= q[0][1]
            q.popleft()
        temp += fruits[position][1]
        result = max(result, temp)
        position += 1
    return result


maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4)
maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4)
maxTotalFruits(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2)
