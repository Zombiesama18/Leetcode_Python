"""
961. 在长度 2N 的数组中找出重复 N 次的元素
给你一个整数数组 nums ，该数组具有以下属性：
nums.length == 2 * n.
nums 包含 n + 1 个 不同的 元素
nums 中恰有一个元素重复 n 次
找出并返回重复了 n 次的那个元素。
"""
import collections
from typing import List


def repeatedNTimes(nums: List[int]) -> int:
    dictionary = collections.Counter(nums)
    for num, freq in dictionary.items():
        if freq == (len(nums) // 2):
            return num


