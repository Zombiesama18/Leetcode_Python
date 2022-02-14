# 581. 最短无序连续子数组
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 请你找出符合题意的 最短 子数组，并输出它的长度。
def findUnsortedSubarray(nums: [int]) -> int:
    length = len(nums)
    minValue, maxValue, left, right = float('INF'), float('-INF'), -1, -1
    for i in range(length):
        if maxValue > nums[i]:
            right = i
        else:
            maxValue = nums[i]
        if minValue < nums[length - i - 1]:
            left = length - i - 1
        else:
            minValue = nums[length - i - 1]
    return 0 if right == -1 else right - left + 1


findUnsortedSubarray([2,6,4,8,10,9,15])
