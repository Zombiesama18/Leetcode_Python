"""
969. 煎饼排序
给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。
一次煎饼翻转的执行过程如下：
选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。
以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。
"""
from typing import *


def pancakeSort(arr: List[int]) -> List[int]:
    result = []
    right = len(arr) - 1
    while right > 0:
        index = arr.index(max(arr[0: right + 1]))
        if index == right:
            right -= 1
            continue
        if index != 0:
            arr = list(reversed(arr[: index + 1])) + arr[index + 1:]
            result.append(index + 1)
        arr = list(reversed(arr[: right + 1])) + arr[right + 1:]
        result.append(right + 1)
        right -= 1
    return result



pancakeSort([3,2,4,1])
