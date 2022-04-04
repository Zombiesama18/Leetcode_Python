"""
2210. 统计数组中峰和谷的数量
给你一个下标从 0 开始的整数数组 nums 。如果两侧距 i 最近的不相等邻居的值均小于 nums[i] ，则下标 i 是 nums 中，某个峰的一部分。
类似地，如果两侧距 i 最近的不相等邻居的值均大于 nums[i] ，则下标 i 是 nums 中某个谷的一部分。对于相邻下标 i 和 j ，
如果 nums[i] == nums[j] ， 则认为这两下标属于 同一个 峰或谷。
注意，要使某个下标所做峰或谷的一部分，那么它左右两侧必须 都 存在不相等邻居。
返回 nums 中峰和谷的数量。
"""
from typing import List


def countHillValley(nums: List[int]) -> int:
    modifiedNums = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != modifiedNums[-1]:
            modifiedNums.append(nums[i])
    counter = 0
    for i in range(1, len(modifiedNums) - 1):
        if modifiedNums[i - 1] < modifiedNums[i] > modifiedNums[i + 1] or \
                modifiedNums[i - 1] > modifiedNums[i] < modifiedNums[i + 1]:
            counter += 1
    return counter
