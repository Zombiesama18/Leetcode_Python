"""
689. 三个无重叠子数组的最大和
给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。
以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
"""


def maxSumOfThreeSubarrays(nums: [int], k: int) -> [int]:
    """使用三个大小为k的滑动窗口，设sum1为第一个滑动窗口的元素和，从[0, k - 1]开始；sum2为第二个滑动窗口的元素和，从[k, 2k - 1]开始；
    sum3为第三个滑动窗口的元素和，从[2k, 3k - 1]开始。同时向右滑动三个窗口，维护maxSum12及其对应的位置。
    每次滑动时，计算当前maxSum12与sum3的和。统计过程中maxSum12 + sum3的最大值与对应位置"""
    sum1, max_sum1, sum2, max_sum12, sum3, max_total = 0, 0, 0, 0, 0, 0
    max_sum1_idx, max_sum12_idx = 0, ()
    result = []
    for i in range(2 * k, len(nums)):
        sum1 += nums[i - k * 2]
        sum2 += nums[i - k]
        sum3 += nums[i]
        if i >= 3 * k - 1:
            if sum1 > max_sum1:
                max_sum1 = sum1
                max_sum1_idx = i - 3 * k + 1
            if max_sum1 + sum2 > max_sum12:
                max_sum12 = max_sum1 + sum2
                max_sum12_idx = (max_sum1_idx, i - 2 * k + 1)
            if max_sum12 + sum3 > max_total:
                max_total = max_sum12 + sum3
                result = [*max_sum12_idx, i - k + 1]
            sum1 -= nums[i - 3 * k + 1]
            sum2 -= nums[i - 2 * k + 1]
            sum3 -= nums[i - k + 1]
    return result


