# 213. 打家劫舍 II（需要复习）
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
def robSelfMadeButSlow(nums: [int]) -> int:
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)

    def dfs(position: int, currentBenefit: int, maxBenefit: int, useFirst: bool):
        if position == len(nums) - 1:
            if currentBenefit + nums[position] > maxBenefit:
                if useFirst:
                    return maxBenefit
                else:
                    return currentBenefit + nums[position]
            else:
                return maxBenefit
        if position == len(nums) - 2:
            if currentBenefit + nums[position] > maxBenefit:
                return currentBenefit + nums[position]
            else:
                return maxBenefit
        currentBenefit = currentBenefit + nums[position]
        maxBenefit = max(currentBenefit, maxBenefit)
        for i in range(position + 2, min(position + 5, len(nums))):
            maxBenefit = dfs(i, currentBenefit, maxBenefit, useFirst)
        return maxBenefit

    result = dfs(0, 0, 0, True)
    result = max(dfs(1, 0, 0, False), result)
    result = max(dfs(2, 0, 0, False), result)
    return result


numss = [[4, 1, 2, 7, 5, 3, 1], [2, 3, 2], [1, 2, 3, 1], [2, 1], [0]]
for nums in numss:
    print('输入：{}\t结果：{}'.format(nums, robSelfMadeButSlow(nums)))


# [4,1,2,7,5,3,1]一行动态规划列出来就懂了
def rob(nums: [int]) -> int:
    def robRange(start: int, end: int):
        first = nums[start]
        second = max(nums[start + 1], first)
        for i in range(start + 2, end + 1):
            first, second = second, max(first + nums[i], second)
        return second

    length = len(nums)
    if length == 0:
        return 0
    if length < 3:
        return max(nums)
    return max(robRange(0, length - 2), robRange(1, length - 1))


numss = [[4, 1, 2, 7, 5, 3, 1], [2, 3, 2], [1, 2, 3, 1], [2, 1], [0]]
for nums in numss:
    print('输入：{}\t结果：{}'.format(nums, rob(nums)))
