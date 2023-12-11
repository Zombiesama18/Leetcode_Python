"""
1005. K 次取反后最大化的数组和
给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
以这种方式修改数组后，返回数组 可能的最大和 。
"""
import heapq


def largestSumAfterKNegations(nums: [int], k: int) -> int:
    nums.sort()
    index = 0
    while index < len(nums) and nums[index] < 0 and k > 0:
        nums[index] = -nums[index]
        k -= 1
        index += 1
    if k % 2 == 0:
        return sum(nums)
    else:
        result = sum(nums)
        if index == 0:
            result -= nums[index] * 2
        elif index == len(nums):
            result -= nums[index - 1] * 2
        else:
            result -= min(nums[index - 1], nums[index]) * 2
    return result


largestSumAfterKNegations([3,-1,0,2], 3)
largestSumAfterKNegations([-2,9,9,8,4], 5)
largestSumAfterKNegations([5,6,9,-3,3], 2)
largestSumAfterKNegations([-4,-2,-3], 4)
