"""
2216. 美化数组的最少删除数
给你一个下标从 0 开始的整数数组 nums ，如果满足下述条件，则认为数组 nums 是一个 美丽数组 ：
nums.length 为偶数
对所有满足 i % 2 == 0 的下标 i ，nums[i] != nums[i + 1] 均成立
注意，空数组同样认为是美丽数组。
你可以从 nums 中删除任意数量的元素。当你删除一个元素时，被删除元素右侧的所有元素将会向左移动一个单位以填补空缺，而左侧的元素将会保持 不变 。
返回使 nums 变为美丽数组所需删除的 最少 元素数目。
"""
from typing import List


def minDeletion(nums: List[int]) -> int:
    index = 0
    result = 0
    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            result += 1
        else:
            index += 1
        index += 1
    if (len(nums) - result) % 2 == 1:
        result += 1
    return result
