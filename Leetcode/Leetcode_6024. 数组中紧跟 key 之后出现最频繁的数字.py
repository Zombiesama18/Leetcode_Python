"""
6024. 数组中紧跟 key 之后出现最频繁的数字
给你一个下标从 0 开始的整数数组 nums ，同时给你一个整数 key ，它在 nums 出现过。
统计 在 nums 数组中紧跟着 key 后面出现的不同整数 target 的出现次数。换言之，target 的出现次数为满足以下条件的 i 的数目：
0 <= i <= n - 2
nums[i] == key 且
nums[i + 1] == target 。
请你返回出现 最多 次数的 target 。测试数据保证出现次数最多的 target 是唯一的。
"""
import collections
from typing import List


def mostFrequent(nums: List[int], key: int) -> int:
    dictionary = collections.defaultdict(int)
    index = 0
    while index < len(nums) - 1:
        if nums[index] == key:
            dictionary[nums[index + 1]] += 1
        index += 1
    return max(dictionary.keys(), key=lambda x: dictionary[x])

