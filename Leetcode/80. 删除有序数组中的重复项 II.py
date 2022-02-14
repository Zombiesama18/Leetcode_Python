# 80. 删除有序数组中的重复项 II
# 给你一个有序数组 nums1 ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
def removeDuplicates(nums: [int]) -> int:
    counterForThisDigit = 1
    index = 1
    while index < len(nums):
        if nums[index] == nums[index - 1]:
            if counterForThisDigit == 2:
                nums.pop(index)
            else:
                counterForThisDigit += 1
                index += 1
        else:
            counterForThisDigit = 1
            index += 1
    return index


nums1 = [1, 1, 1, 2, 2, 3]
removeDuplicates(nums1)
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
removeDuplicates(nums2)


def removeDuplicatesVersion2(nums: [int]) -> int:
    index = 0
    for num in nums:
        if index < 2 or nums[index - 2] < num:
            nums[index] = num
            index += 1
    while len(nums) != index:
        nums.pop(-1)
    return index


nums1 = [1, 1, 1, 2, 2, 3]
removeDuplicatesVersion2(nums1)
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
removeDuplicatesVersion2(nums2)
