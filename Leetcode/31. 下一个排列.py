# 31. 下一个排列
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间


def nextPermutation(nums):
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            temp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = temp
            return nums
    nums.sort()
    return nums


nums = [3, 2, 1]
nextPermutation(nums)
