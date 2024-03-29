"""
1331. 数组序号转换
给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。
序号代表了一个元素有多大。序号编号的规则如下：
序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。
"""
from typing import List


def arrayRankTransform(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    index = 1
    index_dict = {}
    for num in sorted_arr:
        if num not in index_dict:
            index_dict[num] = index
            index += 1
    return [index_dict[num] for num in arr]
