# 169. 多数元素
# 给定一个大小为 n1 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n1/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
def majorityElement(nums):
    length = len(nums)
    history = []
    for i in nums:
        if i not in history:
            history.append(i)
            if nums.count(i) > (length / 2):
                return i
    return 'No Majoritylement'


nums = [3, 2, 3]
majorityElement(nums)
nums = [2, 2, 1, 1, 1, 2, 2]
majorityElement(nums)
