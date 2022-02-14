"""
5977. 最少交换次数来组合所有的 1 II
交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。
环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。
给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。
"""
import random
from typing import List


def minSwaps(nums: List[int]) -> int:
    counter = nums.count(1)
    if counter == len(nums) or counter == 1 or counter == 0:
        return 0
    window = 0
    for i in range(counter):
        window += nums[i]
    result = counter - window
    for i in range(len(nums)):
        window += nums[(i + counter) % len(nums)]
        window -= nums[i]
        result = min(result, counter - window)
    return result



