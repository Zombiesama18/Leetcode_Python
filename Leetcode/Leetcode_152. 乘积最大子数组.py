# 152. 乘积最大子数组
# 给你一个整数数组 nums1 ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
def maxProduct(nums):
    subsets = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subsets.append(nums[i:j])
    output = []
    for i in subsets:
        temp = 1
        for j in i:
            temp = temp * j
        output.append(temp)
    return max(output)


nums = [2, 3, -2, 4]
maxProduct(nums)
nums = [-2, 0, -1]
maxProduct(nums)
