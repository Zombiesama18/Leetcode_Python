# 154. 寻找旋转排序数组中的最小值 II
# 已知一个长度为 n1 的数组，预先按照升序排列，经由 1 到 n1 次 旋转 后，得到输入数组。
# 例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n1-1]] 旋转一次 的结果为数组 [a[n1-1], a[0], a[1], a[2], ..., a[n1-2]] 。
# 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
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


nums1 = [1,3,5]
findMin(nums1)
nums2 = [2,2,2,0,1]
findMin(nums2)


# 在二分查找的每一步中，左边界为low，右边界为high，区间的中点为pivot，最小值就在该区间内。
# 我们将中轴元素nums[pivot] 与右边界元素nums[high] 进行比较，可能会有以下的三种情况：
# 第一种情况是 nums[pivot]<nums[high]。这说明 nums[pivot] 是最小值右侧的元素，因此我们可以忽略二分查找区间的右半部分。
# 第二种情况是 nums[pivot]>nums[high]。这说明nums[pivot] 是最小值左侧的元素，因此我们可以忽略二分查找区间的左半部分。
# 第三种情况是 nums[pivot]==nums[high]。由于重复元素的存在，我们并不能确定 nums[pivot] 究竟在最小值的左侧还是右侧，
# 因此我们不能莽撞地忽略某一部分的元素。我们唯一可以知道的是，由于它们的值相同，所以无论 nums[high] 是不是最小值，
# 都有一个它的「替代品」nums[pivot]，因此我们可以忽略二分查找区间的右端点。
def findMinVersion2(nums: [int]) -> int:
    if not nums:
        return nums
    length = len(nums)
    if length == 1:
        return nums[0]
    left, right = 0, length - 1
    while left < right:
        pivot = (left + right) >> 1
        if nums[pivot] < nums[right]:
            right = pivot
        elif nums[pivot] > nums[right]:
            left = pivot + 1
        else:
            right -= 1
    return nums[left]


nums1 = [1,3,5]
findMinVersion2(nums1)
nums2 = [2,2,2,0,1]
findMinVersion2(nums2)
