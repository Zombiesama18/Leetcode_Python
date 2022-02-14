"""
786. 第 K 个最小的素数分数
给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。
"""
import heapq


def kthSmallestPrimeFraction(arr: [int], k: int) -> [int]:
    class Fraction:
        def __init__(self, idx, idy, x, y):
            self.idx = idx
            self.idy = idy
            self.x = x
            self.y = y

        def __lt__(self, other: 'Fraction'):
            return self.x * other.y < self.y * other.x

    length = len(arr)
    q = [Fraction(0, i, arr[0], arr[i]) for i in range(1, length)]
    heapq.heapify(q)
    for _ in range(k - 1):
        fraction = heapq.heappop(q)
        idx, idy = fraction.idx, fraction.idy
        if idx + 1 < idy:
            heapq.heappush(q, Fraction(idx + 1, idy, arr[idx + 1], arr[idy]))
    return [q[0].x, q[0].y]

