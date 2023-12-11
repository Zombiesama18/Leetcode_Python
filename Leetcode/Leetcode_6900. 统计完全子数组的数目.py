"""
6900. 统计完全子数组的数目

给你一个由 正 整数组成的数组 nums 。
如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：
子数组中 不同 元素的数目等于整个数组不同元素的数目。
返回数组中 完全子数组 的数目。
子数组 是数组中的一个连续非空序列。
"""
import collections
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        target_number = len(counter.keys())
        counter = collections.Counter()
        left, right = 0, 0
        result = 0
        while right < len(nums):
            result += left
            counter[nums[right]] += 1
            while len(counter) == target_number:
                result += 1
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            right += 1
        return result

Solution().countCompleteSubarrays([1,3,1,2,2])
Solution().countCompleteSubarrays([5, 5, 5, 5])
