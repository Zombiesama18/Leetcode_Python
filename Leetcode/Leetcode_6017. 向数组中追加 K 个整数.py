"""
6017. 向数组中追加 K 个整数
给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。
返回追加到 nums 中的 k 个整数之和。
"""
from typing import List


def minimalKSum(nums: List[int], k: int) -> int:
    nums.sort()
    rightSide = k
    result = k * (1 + k) // 2
    visited = set()
    for num in nums:
        if num <= rightSide and num not in visited:
            rightSide += 1
            result += rightSide - num
            visited.add(num)
        elif num > rightSide:
            break
    return result


minimalKSum([96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84], 35)
