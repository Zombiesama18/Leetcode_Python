"""
2321. 拼接数组的最大分数
给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度都是 n 。
你可以选择两个整数 left 和 right ，其中 0 <= left <= right < n ，
接着 交换 两个子数组 nums1[left...right] 和 nums2[left...right] 。
例如，设 nums1 = [1,2,3,4,5] 和 nums2 = [11,12,13,14,15] ，整数选择 left = 1 和 right = 2，
那么 nums1 会变为 [1,12,13,4,5] 而 nums2 会变为 [11,2,3,14,15] 。
你可以选择执行上述操作 一次 或不执行任何操作。
数组的 分数 取 sum(nums1) 和 sum(nums2) 中的最大值，其中 sum(arr) 是数组 arr 中所有元素之和。
返回 可能的最大分数 。
子数组 是数组中连续的一个元素序列。arr[left...right] 表示子数组包含 nums 中下标 left 和 right
之间的元素（含 下标 left 和 right 对应元素）。
"""
from typing import List


def maximumsSplicedArray(nums1: List[int], nums2: List[int]) -> int:
    one_over_two = [0, 0]
    two_over_one = [0, 0]
    for i in range(len(nums1)):
        difference = nums1[i] - nums2[i]
        if difference > 0:
            one_over_two[-1] += difference
            two_over_one[-1] -= difference
            if two_over_one[-1] < 0:
                two_over_one[-1] = 0
            one_over_two[0] = max(one_over_two)
        elif difference < 0:
            one_over_two[-1] += difference
            if one_over_two[-1] < 0:
                one_over_two[-1] = 0
            two_over_one[-1] -= difference
            two_over_one[0] = max(two_over_one)
    return max(sum(nums1) + two_over_one[0], sum(nums2) + one_over_two[0])


maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10])

