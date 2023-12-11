"""
1053. 交换一次的先前排列

给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、
按字典序排列小于 arr 的最大排列。
如果无法这么操作，就请返回原数组。
"""
from typing import List


def prevPermOpt1(arr: List[int]) -> List[int]:
    index = 1
    idx1, idx2 = None, None
    while index < len(arr):
        if arr[index] < arr[index - 1]:
            idx1 = index - 1
            idx2 = index
        elif idx1 is not None and arr[index] < arr[idx1]:
            idx2 = index
        index += 1
    if idx1 is not None:
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


prevPermOpt1([3,1,1,3])


