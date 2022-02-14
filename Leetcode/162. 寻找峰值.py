# 162. 寻找峰值
# 峰值元素是指其值严格大于左右相邻值的元素。
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
import random


def findPeakElement(nums: [int]) -> int:
    nums.insert(0, float('-INF'))
    nums.append(float('-INF'))
    length = len(nums)
    for i in range(1, length - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i - 1


def findPeakElementRandomStart(nums: [int]) -> int:
    length = len(nums)
    index = random.randint(0, length - 1)

    def getItem(idx: int):
        if idx == -1 or idx == length:
            return float('-INF')
        return nums[idx]

    while not (getItem(index - 1) < getItem(index) > getItem(index + 1)):
        if getItem(index) < getItem(index + 1):
            index += 1
        else:
            index -= 1
    return index



