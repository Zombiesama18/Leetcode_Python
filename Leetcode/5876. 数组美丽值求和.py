# 5876. 数组美丽值求和（需要复习）
# 给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：
# 2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]
# 1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件
# 0，如果上述条件全部不满足
# 返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。
def sumOfBeauties(nums: [int]) -> int:
    length = len(nums)
    maxFromStart = [0 for _ in range(length)]
    maxFromStart[0] = nums[0]
    minFromEnd = [0 for _ in range(length)]
    minFromEnd[length - 1] = nums[length - 1]
    for i in range(1, length - 1):
        maxFromStart[i] = max(nums[i], maxFromStart[i - 1])
        minFromEnd[length - i - 1] = min(minFromEnd[length - i], nums[length - i - 1])
    counter = 0
    for i in range(1, length - 1):
        if maxFromStart[i - 1] < nums[i] < minFromEnd[i + 1]:
            counter += 2
        elif nums[i - 1] < nums[i] < nums[i + 1]:
            counter += 1
    return counter


sumOfBeauties([1,2,3])
sumOfBeauties([2,4,6,4])
sumOfBeauties([3,2,1])
sumOfBeauties([1,2,3,4,5,7,8,9,10])



