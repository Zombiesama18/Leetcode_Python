# 421. 数组中两个数的最大异或值
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
def findMaximumXOR(nums: [int]) -> int:
    maxValue = float('-INF')
    length = len(nums)
    if length == 1:
        return nums[0]
    for i in range(length - 1):
        for j in range(i, length):
            maxValue = max(maxValue, nums[i] ^ nums[j])
    return maxValue


findMaximumXOR([3, 10, 5, 25, 2, 8])
findMaximumXOR([0])
findMaximumXOR([2, 4])
findMaximumXOR([8, 10, 2])
findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])
