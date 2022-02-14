# 377. 组合总和 Ⅳ（需要复习）
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
#
# 题目数据保证答案符合 32 位整数范围。
def combinationSum4ByDemonstratingAllResult(nums: [int], target: int) -> int:
    result = []

    def combinationHelper(currentSum: int, currentCombination: [int]):
        if currentSum > target:
            return True
        if currentSum == target:
            result.append(currentCombination.copy())
            return True
        for num in nums:
            if combinationHelper(currentSum + num, currentCombination + [num]):
                break
        return

    for num in nums:
        combinationHelper(num, [num])
    return len(result)


def combinationSum4ByCounting(nums: [int], target: int) -> int:
    result = 0
    nums.sort()

    def combinationHelper(currentSum: int, counter: int):
        if currentSum > target:
            return True, counter
        if currentSum == target:
            counter += 1
            return True, counter
        for num in nums:
            flag, counter = combinationHelper(currentSum + num, counter)
            if flag:
                break
        return False, counter

    for num in nums:
        _, result = combinationHelper(num, result)
    return result


def combinationSum4ByDynamicProgramming(nums: [int], target: int) -> int:
    dp = [1] + [0] * target
    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]
    return dp[target]


nums = [4,2,1]
target = 32
# combinationSum4ByDemonstratingAllResult(nums, target)
# combinationSum4ByCounting(nums, target)
combinationSum4ByDynamicProgramming(nums, target)

