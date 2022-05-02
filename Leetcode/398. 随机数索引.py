"""
398. 随机数索引
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
"""
import collections
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.dictionary = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.dictionary[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dictionary[target])
