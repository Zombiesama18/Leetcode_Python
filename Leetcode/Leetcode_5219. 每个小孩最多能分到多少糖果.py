"""
5219. 每个小孩最多能分到多少糖果
给你一个 下标从 0 开始 的整数数组 candies 。数组中的每个元素表示大小为 candies[i] 的一堆糖果。你可以将每堆糖果分成任意数量的 子堆 ，
但 无法 再将两堆合并到一起。
另给你一个整数 k 。你需要将这些糖果分配给 k 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。
返回每个小孩可以拿走的 最大糖果数目 。
"""
from typing import List


def maximumCandies(candies: List[int], k: int) -> int:
    def check(target):
        if target == 0:
            return True
        counter = 0
        for candy in candies:
            counter += candy // target
            if counter >= k:
                return True
        return False

    left, right = 0, sum(candies)
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left


maximumCandies([5,8,6], 3)
maximumCandies([4,7,5], 4)
