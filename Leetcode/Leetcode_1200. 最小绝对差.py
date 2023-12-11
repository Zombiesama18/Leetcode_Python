"""
1200. 最小绝对差
给你个整数数组 arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
"""
from typing import List


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    arr.sort()
    difference = float('INF')
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < difference:
            result = [[arr[i - 1], arr[i]]]
            difference = arr[i] - arr[i - 1]
        elif arr[i] - arr[i - 1] == difference:
            result.append([arr[i - 1], arr[i]])
    return result

