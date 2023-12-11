# 494. 目标和（绕一个弯的动态规划）
# 给你一个整数数组 nums 和一个整数 target 。
# 
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

# 记数组的元素和为 sum，添加 - 号的元素之和为 neg，则其余添加 + 的元素之和为 sum−neg，得到的表达式的结果为
# (sum - neg) - neg = sum - 2 * neg = target， 即 neg = (sum - target) / 2
# 由于数组 nums 中的元素都是非负整数，neg 也必须是非负整数，所以上式成立的前提是 sum−target 是非负偶数。若不符合该条件可直接返回 0。
# 若上式成立，问题转化成在数组 nums 中选取若干元素，使得这些元素之和等于 neg，计算选取元素的方案数。我们可以使用动态规划的方法求解。
# 定义二维数组 dp，其中 dp[i][j] 表示在数组 nums 的前 i 个数中选取元素，使得这些元素之和等于 j 的方案数。假设数组 nums 的长度为 n，则最终答案为 dp[n][neg]。

def findTargetSumWays(nums: [int], target: int) -> int:
    length = len(nums)
    if length < 1:
        return 0
    arraySum = sum(nums)
    sumMinusTarget = arraySum - target
    if sumMinusTarget < 0 or sumMinusTarget % 2 != 0:
        return 0
    sumToBeNegative = sumMinusTarget // 2
    dynamicPlanningSpace = [[0] * (sumToBeNegative + 1) for _ in range(length + 1)]
    dynamicPlanningSpace[0][0] = 1
    for i in range(1, length + 1):
        currentNum = nums[i - 1]
        for j in range(sumToBeNegative + 1):
            dynamicPlanningSpace[i][j] += dynamicPlanningSpace[i - 1][j]
            if j >= currentNum:
                dynamicPlanningSpace[i][j] += dynamicPlanningSpace[i - 1][j - currentNum]
    return dynamicPlanningSpace[length][sumToBeNegative]


findTargetSumWays([1,1,1,1,1], 3)





