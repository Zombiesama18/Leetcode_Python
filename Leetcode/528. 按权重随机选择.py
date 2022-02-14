# 528. 按权重随机选择
# 给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，
# 选取下标 i 的概率与 w[i] 成正比。
# 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。
# 也就是说，选取下标 i 的概率为 w[i] / sum(w) 。
import random


class Solution:
    def __init__(self, w: [int]):
        self.sum = w[0]
        self.sumOfNItems = [w[0]]
        for i in range(1, len(w)):
            self.sumOfNItems.append(w[i] + self.sumOfNItems[-1])
            self.sum += w[i]

    def pickIndex(self) -> int:
        randomNumber = random.randint(0, self.sum - 1)
        left, right = 0, len(self.sumOfNItems) - 1
        while left < right:
            mid = (left + right) // 2
            if self.sumOfNItems[mid] > randomNumber:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution([1, 3, 2])
s.pickIndex()
