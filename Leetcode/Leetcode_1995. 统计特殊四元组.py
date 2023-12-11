"""
1995. 统计特殊四元组
给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
nums[a] + nums[b] + nums[c] == nums[d] ，且
a < b < c < d
"""
import collections


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        counter = collections.Counter()
        for c in range(len(nums) - 2, -1, -1):
            counter[nums[c + 1]] += 1
            for a in range(c):
                for b in range(a + 1, c):
                    if (d := nums[a] + nums[b] + nums[c]) in counter:
                        result += counter[d]
        return result
