"""
5990. 找出数组中的所有孤独数字
给你一个整数数组 nums 。如果数字 x 在数组中仅出现 一次 ，且没有 相邻 数字（即，x + 1 和 x - 1）出现在数组中，则认为数字 x 是 孤独数字 。
返回 nums 中的 所有 孤独数字。你可以按 任何顺序 返回答案。
"""
import collections
from typing import List


def findLonely(nums: List[int]) -> List[int]:
    dictionary = collections.Counter(nums)
    result = []
    for num in dictionary:
        if dictionary[num] == 1 and num + 1 not in dictionary and num - 1 not in dictionary:
            result.append(num)
    return result
