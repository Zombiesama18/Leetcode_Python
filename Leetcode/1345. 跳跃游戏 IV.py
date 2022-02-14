"""
1345. 跳跃游戏 IV
给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
每一步，你可以从下标 i 跳到下标：
i + 1 满足：i + 1 < arr.length
i - 1 满足：i - 1 >= 0
j 满足：arr[i] == arr[j] 且 i != j
请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
注意：任何时候你都不能跳到数组外面。
"""
import collections
from typing import List


def minJumps(arr: List[int]) -> int:
    dictionary = collections.defaultdict(list)
    for i in range(len(arr)):
        dictionary[arr[i]].append(i)
    q = collections.deque([(0, 0)])
    visited = {0}
    while q:
        currentPosition, steps = q.popleft()
        if currentPosition == len(arr) - 1:
            return steps
        for nextPosition in dictionary[arr[currentPosition]]:
            if nextPosition not in visited:
                q.append((nextPosition, steps + 1))
                visited.add(nextPosition)
        del dictionary[arr[currentPosition]]  # 关键在于del 掉查找过的，防止重复搜索
        if currentPosition + 1 < len(arr) and currentPosition + 1 not in visited:
            q.append((currentPosition + 1, steps + 1))
            visited.add(currentPosition + 1)
        if currentPosition - 1 > 0 and currentPosition - 1 not in visited:
            q.append((currentPosition - 1, steps + 1))
            visited.add(currentPosition - 1)






