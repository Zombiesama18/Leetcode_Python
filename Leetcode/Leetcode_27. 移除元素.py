# 27. 移除元素
# 给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
def removeElement(nums: [int], val: int) -> int:
    if not nums:
        return 0
    length = len(nums)
    slowPointer = 0
    fastPointer = 0
    while fastPointer < length:
        if nums[fastPointer] != val:
            nums[slowPointer] = nums[fastPointer]
            slowPointer += 1
        fastPointer += 1
    nums = nums[:slowPointer]
    return slowPointer


numss = [[3, 2, 2, 3], [0, 1, 2, 2, 3, 0, 4, 2]]
vals = [3, 2]
for i in range(len(numss)):
    print('input: nums = {}, val = \toutput: length = {}, nums = {}'.format(numss[i], vals[i],
                                                                            removeElement(numss[i], vals[i]), numss[i]))

