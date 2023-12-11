# 53. 最大子序和
# 给定一个整数数组 nums1 ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


def maxSubArray(nums):
    subsets = []

    def get_cont_subsets():
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subsets.append(nums[i: j])

    get_cont_subsets()
    sums = []
    for i in subsets:
        sums.append(sum(i))
    return max(sums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray(nums)
