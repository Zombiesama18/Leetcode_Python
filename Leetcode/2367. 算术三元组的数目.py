"""
2367. 算术三元组的数目

给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：
i < j < k ，
nums[j] - nums[i] == diff 且
nums[k] - nums[j] == diff
返回不同 算术三元组 的数目。
"""
import bisect
from typing import List


def arithmeticTriplets(nums: List[int], diff: int) -> int:
    result = 0
    for i in range(len(nums) - 2):
        target1 = nums[i] + diff
        index1 = bisect.bisect_left(nums[i + 1:], target1)
        if i + index1 + 1 < len(nums) and nums[i + index1 + 1] == target1:
            target2 = target1 + diff
            index2 = bisect.bisect_left(nums[i + index1 + 2:], target2)
            if i + index1 + 2 + index2 < len(nums) and nums[i + index1 + 2 + index2] == target2:
                result += 1
    return result


arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2)
arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3)
