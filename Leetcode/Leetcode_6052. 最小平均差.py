"""
6052. 最小平均差
给你一个下标从 0 开始长度为 n 的整数数组 nums 。
下标 i 处的 平均差 指的是 nums 中 前 i + 1 个元素平均值和 后 n - i - 1 个元素平均值的 绝对差 。两个平均值都需要 向下取整 到最近的整数。
请你返回产生 最小平均差 的下标。如果有多个下标最小平均差相等，请你返回 最小 的一个下标。
注意：
两个数的 绝对差 是两者差的绝对值。
 n 个元素的平均值是 n 个元素之 和 除以（整数除法） n 。
0 个元素的平均值视为 0 。
"""
from typing import List


def minimumAverageDifference(nums: List[int]) -> int:
    leftSum, rightSum = 0, sum(nums)
    leftNum, rightNum = 0, len(nums)
    result = 0
    minAbsDifference = float('INF')
    for i in range(len(nums) - 1):
        leftSum += nums[i]
        rightSum -= nums[i]
        leftNum += 1
        rightNum -= 1
        absDifference = abs(leftSum // leftNum - rightSum // rightNum)
        if absDifference < minAbsDifference:
            minAbsDifference = absDifference
            result = i
    if (leftSum + nums[-1]) // len(nums) < minAbsDifference:
        result = len(nums) - 1
    return result


minimumAverageDifference([2,5,3,9,5,3])
