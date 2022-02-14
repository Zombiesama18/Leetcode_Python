# 26. 删除有序数组中的重复项
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
def removeDuplicates(nums: [int]) -> int:
    length = len(nums)
    index = 0
    while index < length - 1:
        if nums[index] == nums[index + 1]:
            nums.pop(index + 1)
            length -= 1
        else:
            index += 1
    return length


numss = [[1,1,2], [0,0,1,1,1,2,2,3,3,4]]
for nums in numss:
    print('输入：{}\t输出：len:{},nums:{}'.format(nums, removeDuplicates(nums), nums))


def removeDuplicatesDoublePointer(nums: [int]) -> int:
    if not nums:
        return 0
    slowPointer = 1
    fastPointer = 1
    length = len(nums)
    while fastPointer < length:
        if nums[fastPointer] != nums[fastPointer - 1]:
            nums[slowPointer] = nums[fastPointer]
            slowPointer += 1
        fastPointer += 1
    nums = nums[:slowPointer]
    return slowPointer


numss = [[1,1,2], [0,0,1,1,1,2,2,3,3,4]]
for nums in numss:
    print('输入：{}\t输出：len:{},nums:{}'.format(nums, removeDuplicatesDoublePointer(nums), nums))
