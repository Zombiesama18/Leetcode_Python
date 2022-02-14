# 673. 最长递增子序列的个数
# 给定一个未排序的整数数组，找到最长递增子序列的个数。‘
def findNumberOfLIS(nums: [int]) -> int:
    length = len(nums)
    longest = 0
    dp = [1 for _ in range(length)]
    counter = [1 for _ in range(length)]
    for i in range(length):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    counter[i] = counter[j]
                elif dp[j] + 1 == dp[i]:
                    counter[i] += counter[j]
        longest = max(longest, dp[i])
    result = 0
    for index, value in enumerate(dp):
        if dp[index] == longest:
            result += counter[index]
    return result


findNumberOfLIS([1,3,5,4,7])
findNumberOfLIS([2,2,2,2,2])
