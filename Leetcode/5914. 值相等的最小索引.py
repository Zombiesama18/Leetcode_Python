# 5914. 值相等的最小索引
# 给你一个下标从 0 开始的整数数组 nums ，返回 nums 中满足 i mod 10 == nums[i] 的最小下标 i ；如果不存在这样的下标，返回 -1 。
# x mod y 表示 x 除以 y 的 余数 。
def smallestEqual(nums: [int]) -> int:
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1


smallestEqual([0,1,2])
smallestEqual([4,3,2,1])
smallestEqual([1,2,3,4,5,6,7,8,9,0])
smallestEqual([2,1,3,5,2])

