# 1991. 找到数组的中间位置
# 给你一个下标从 0 开始的整数数组 nums ，请你找到 最左边 的中间位置 middleIndex （也就是所有可能中间位置下标最小的一个）。
# 中间位置 middleIndex 是满足 nums[0] + nums[1] + ... + nums[middleIndex-1] ==
# nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1] 的数组下标。
# 如果 middleIndex == 0 ，左边部分的和定义为 0 。类似的，如果 middleIndex == nums.length - 1 ，右边部分的和定义为 0 。
# 请你返回满足上述条件 最左边 的 middleIndex ，如果不存在这样的中间位置，请你返回 -1 。
from itertools import accumulate


def findMiddleIndex(nums: [int]) -> int:
    sumOfNums = sum(nums)
    length = len(nums)
    counter = 0
    for i in range(length):
        if counter == sumOfNums - nums[i]:
            return i
        counter += nums[i]
        sumOfNums -= nums[i]
    return -1


findMiddleIndex([2,3,-1,8,4])
findMiddleIndex([1,-1,4])
findMiddleIndex([2,5])
