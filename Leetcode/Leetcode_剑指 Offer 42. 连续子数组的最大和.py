# 剑指 Offer 42. 连续子数组的最大和
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。
def maxSubArray(nums: [int]) -> int:
    maxResult, pre = nums[0], 0
    for num in nums:
        pre = max(pre + num, num)
        maxResult = max(maxResult, pre)
    return maxResult


maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


