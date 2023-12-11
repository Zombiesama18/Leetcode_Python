# 268. 丢失的数字
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
def missingNumber(nums: [int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)


