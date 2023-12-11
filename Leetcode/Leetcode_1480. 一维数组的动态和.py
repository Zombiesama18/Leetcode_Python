# 1480. 一维数组的动态和
# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
# 请返回 nums 的动态和。
def runningSum(nums: [int]) -> [int]:
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(nums[i] + result[-1])
    return result

