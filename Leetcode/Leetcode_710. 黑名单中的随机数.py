"""
710. 黑名单中的随机数
给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入
黑名单 blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
优化你的算法，使它最小化调用语言 内置 随机函数的次数。
实现 Solution 类:
Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
"""
import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)
        black_over_bound = {number for number in blacklist if number >= self.bound}
        self.map = {}
        map_to = self.bound
        for number in blacklist:
            if number < self.bound:
                while map_to in black_over_bound:
                    map_to += 1
                self.map[number] = map_to
                map_to += 1

    def pick(self) -> int:
        result = random.randrange(0, self.bound)
        return self.map.get(result, result)
