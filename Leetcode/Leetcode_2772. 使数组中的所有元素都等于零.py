"""
2772. 使数组中的所有元素都等于零
给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。
你可以对数组执行下述操作 任意次 ：
从数组中选出长度为 k 的 任一 子数组，并将子数组中每个元素都 减去 1 。
如果你可以使数组中的所有元素都等于 0 ，返回  true ；否则，返回 false 。
子数组 是数组中的一个非空连续元素序列。
"""
from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        differences = [0] * (len(nums) + 1)
        sum_d = 0
        for i, num in enumerate(nums):
            sum_d += differences[i]
            num += sum_d
            if num == 0:
                continue
            if num < 0 or i + k > len(nums):
                return False
            sum_d -= num
            differences[i + k] += num
        return True

    def checkArray_2steps(self, nums: List[int], k: int) -> bool:
        differences = [nums[0]]
        for i in range(1, len(nums)):
            differences.append(nums[i] - nums[i - 1])
        for i in range(len(nums) - k):
            if differences[i] == 0:
                continue
            if differences[i] < 0:
                return False
            differences[i + k] += differences[i]

        for i in range(len(nums) - k + 1, len(nums)):
            if differences[i] != 0:
                return False
        return True

Solution().checkArray_2steps(nums = [2,2,3,1,1,0], k = 3)
Solution().checkArray(nums = [1,3,1,1], k = 2)
print(Solution().checkArray_2steps([60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26], 4))
