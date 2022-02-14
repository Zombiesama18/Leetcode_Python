# 740. 删除并获得点数（需要复习）
# 给你一个整数数组 nums ，你可以对它进行一些操作。
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
def deleteAndEarnByDynamicProgramming(nums: [int]) -> int:
    maxValue = max(nums)
    dp = [0] * (maxValue + 1)
    for value in nums:
        dp[value] += value

    def deleteAndEarnHelper(values: [int]) -> int:
        length = len(values)
        firstValue, secondValue = values[0], max(values[0], values[1])
        for i in range(2, length):
            firstValue, secondValue = secondValue, max(firstValue + values[i], secondValue)
        return secondValue

    return deleteAndEarnHelper(dp)


