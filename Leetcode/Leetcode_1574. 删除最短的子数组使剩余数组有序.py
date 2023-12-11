"""
1574. 删除最短的子数组使剩余数组有序

给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
一个子数组指的是原数组中连续的一个子序列。
请你返回满足题目要求的最短子数组的长度
"""
from typing import List


def findLengthOfShortestSubarray(arr: List[int]) -> int:
    right_ptr = len(arr) - 1
    while right_ptr > 0 and arr[right_ptr - 1] <= arr[right_ptr]:
        right_ptr -= 1
    if right_ptr == 0:
        return 0
    result = right_ptr
    for left_ptr in range(len(arr)):
        while right_ptr < len(arr) and arr[right_ptr] < arr[left_ptr]:
            right_ptr += 1
        result = min(result, right_ptr - left_ptr - 1)
        if left_ptr + 1 < len(arr) and arr[left_ptr] > arr[left_ptr + 1]:
            break
    return result
