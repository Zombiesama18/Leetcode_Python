"""
6000. 对奇偶下标分别排序
给你一个下标从 0 开始的整数数组 nums 。根据下述规则重排 nums 中的值：
按 非递增 顺序排列 nums 奇数下标 上的所有值。
举个例子，如果排序前 nums = [4,1,2,3] ，对奇数下标的值排序后变为 [4,3,2,1] 。奇数下标 1 和 3 的值按照非递增顺序重排。
按 非递减 顺序排列 nums 偶数下标 上的所有值。
举个例子，如果排序前 nums = [4,1,2,3] ，对偶数下标的值排序后变为 [2,1,4,3] 。偶数下标 0 和 2 的值按照非递减顺序重排。
返回重排 nums 的值之后形成的数组。
"""
import heapq
from typing import *


def sortEvenOdd(nums: List[int]) -> List[int]:
    oddList, evenList = [], []
    for i in range(len(nums)):
        if i % 2 == 0:
            heapq.heappush(evenList, nums[i])
        else:
            heapq.heappush(oddList, -nums[i])
    result = []
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(heapq.heappop(evenList))
        else:
            result.append(-heapq.heappop(oddList))
    return result


