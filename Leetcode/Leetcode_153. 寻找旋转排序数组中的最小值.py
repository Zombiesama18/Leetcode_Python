# 153. 寻找旋转排序数组中的最小值
# 已知一个长度为 n1 的数组，预先按照升序排列，经由 1 到 n1 次 旋转 后，得到输入数组。
# 例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 4 次，则可以得到 [0,1,2,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n1-1]] 旋转一次 的结果为数组 [a[n1-1], a[0], a[1], a[2], ..., a[n1-2]] 。
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
def findMin(nums: [int]) -> int:
    if not nums:
        return nums
    length = len(nums)
    if length == 1:
        return nums[0]
    for i in range(length - 1):
        if nums[i] < nums[-1]:
            return nums[i]
    return nums[-1]


nums1 = [3, 4, 5, 1, 2]
findMin(nums1)
nums2 = [4, 5, 6, 7, 0, 1, 2]
findMin(nums2)
nums3 = [11, 13, 15, 17]
findMin(nums3)
nums4 = [2, 1]
findMin(nums4)


def findMinOneLineVersion(nums: [int]) -> int:
    return min(nums)
