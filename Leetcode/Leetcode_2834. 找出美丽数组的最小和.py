"""
2834. 找出美丽数组的最小和

给你两个正整数：n 和 target 。
如果数组 nums 满足下述条件，则称其为 美丽数组 。
nums.length == n.
nums 由两两互不相同的正整数组成。
在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。
返回符合条件的美丽数组所可能具备的 最小 和。
"""


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        result = 0
        current_num = 1
        num_counter = 0
        while num_counter < n:
            if current_num * 2 <= target or current_num >= target:
                result += current_num
                num_counter += 1
            current_num += 1
        return result

