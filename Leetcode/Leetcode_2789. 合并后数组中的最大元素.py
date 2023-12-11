"""
2789. 合并后数组中的最大元素

给你一个下标从 0 开始、由正整数组成的数组 nums 。
你可以在数组上执行下述操作 任意 次：
选中一个同时满足 0 <= i < nums.length - 1 和 nums[i] <= nums[i + 1] 的整数 i 。
将元素 nums[i + 1] 替换为 nums[i] + nums[i + 1] ，并从数组中删除元素 nums[i] 。
返回你可以从最终数组中获得的 最大 元素的值。
"""
from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        result = nums[-1]
        index = len(nums) - 1
        while index > 0:
            if nums[index] >= nums[index - 1]:
                nums[index - 1] = nums[index] + nums[index - 1]
            result = max(result, nums[index - 1])
            index -= 1
        return result


Solution().maxArrayValue(nums =[5,3,3])