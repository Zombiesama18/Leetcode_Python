"""
2488. 统计中位数为 K 的子数组
给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。
统计并返回 nums 中的 中位数 等于 k 的非空子数组的数目。
注意：
数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。
"""
import collections
from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    index = nums.index(k)
    result = 1
    difference_dict = collections.defaultdict(int)
    difference_dict[0] += 1
    difference = 0
    for i in range(index + 1, len(nums)):
        if nums[i] > k:
            difference += 1
        else:
            difference -= 1
        difference_dict[difference] += 1
        if difference == 0 or difference == 1:
            result += 1
    difference = 0
    for i in range(index - 1, -1, -1):
        if nums[i] > k:
            difference += 1
        else:
            difference -= 1
        result += difference_dict[0 - difference] + difference_dict[1 - difference]
    return result


countSubarrays(nums = [3,2,1,4,5], k = 4)

