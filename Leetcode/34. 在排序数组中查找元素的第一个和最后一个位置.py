# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums1，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是O(log n1) 级别。
# 如果数组中不存在目标值，返回[-1, -1]。


def searchRange(nums, target):
    if target in nums:
        start = nums.index(target)
        output = [start]
        while nums[start + 1] == target:
            start += 1
        output.append(start)
        return output
    else:
        return [-1, -1]


nums = [5, 7, 7, 8, 10]
target = 8
searchRange(nums, target)
