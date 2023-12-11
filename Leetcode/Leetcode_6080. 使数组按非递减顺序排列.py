"""
6080. 使数组按非递减顺序排列
给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 < i < nums.length 。
重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。
"""
from typing import List


def totalSteps(nums: List[int]) -> int:
    result, stack = 0, []
    for num in nums:
        maxT = 0
        while stack and stack[-1][0] <= num:
            maxT = max(maxT, stack.pop()[1])
        # 累加递增序列
        if stack:
            maxT += 1
        result = max(result, maxT)
        stack.append((num, maxT))
    return result


totalSteps([5,3,4,4,7,3,6,11,8,5,11])
