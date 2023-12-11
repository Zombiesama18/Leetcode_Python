"""
2845. 统计趣味子数组的数目

给你一个下标从 0 开始的整数数组 nums ，以及整数 modulo 和整数 k 。
请你找出并统计数组中 趣味子数组 的数目。
如果 子数组 nums[l..r] 满足下述条件，则称其为 趣味子数组 ：
在范围 [l, r] 内，设 cnt 为满足 nums[i] % modulo == k 的索引 i 的数量。并且 cnt % modulo == k 。
以整数形式表示并返回趣味子数组的数目。
注意：子数组是数组中的一个连续非空的元素序列。
"""
import collections
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        result = 0
        counter = collections.Counter([0])
        sum_of_satisfy = 0
        for num in nums:
            if num % modulo == k:
                sum_of_satisfy += 1
            result += counter[(sum_of_satisfy - k) % modulo]
            counter[sum_of_satisfy % modulo] += 1
        return result


Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)

