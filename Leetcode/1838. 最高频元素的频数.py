# 1838. 最高频元素的频数
# 元素的 频数 是该元素在一个数组中出现的次数。
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
def maxFrequency(nums: [int], k: int) -> int:
    nums.sort()
    left, length, total, result = 0, len(nums), 0, 1
    for i in range(1, length):
        total += (nums[i] - nums[i - 1]) * (i - left)
        while total > k:
            total -= nums[i] - nums[left]
            left += 1
        result = max(result, i - left + 1)
    return result


maxFrequency([1,2,4], 5)
maxFrequency([1,4,8,13], 5)
