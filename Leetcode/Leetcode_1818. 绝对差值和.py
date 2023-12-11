# 1818. 绝对差值和
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
# |x| 定义为：
# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 -x
import bisect


def minAbsoluteSumDiffSlow(nums1: [int], nums2: [int]) -> int:
    base = 1000000007
    absoluteSum = 0
    length = len(nums1)
    for i in range(length):
        absoluteSum = (absoluteSum + abs(nums1[i] - nums2[i])) % base
    minAbsoluteSum = absoluteSum
    for i in range(length):
        for j in range(length):
            minAbsoluteSum = min(absoluteSum - (abs(nums1[j] - nums2[j]) - abs(nums1[i] - nums2[j])), minAbsoluteSum) % base
    return minAbsoluteSum


minAbsoluteSumDiffSlow([1, 7, 5], [2, 3, 5])
minAbsoluteSumDiffSlow([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4])


def minAbsoluteSumDiffBinarySearch(nums1: [int], nums2: [int]) -> int:
    def binarySearch(targetList: [int], targetElement: int):
        left, right = 0, len(targetList) - 1
        if targetList[right] < targetElement:
            return right + 1
        while left < right:
            mid = (left + right) // 2
            if targetList[mid] < targetElement:
                left = mid + 1
            else:
                right = mid
        return left

    mod, length, absoluteSum, maxn = 1000000007, len(nums1), 0, 0
    length = len(nums1)
    tempList = nums1[:]
    tempList.sort()
    for i in range(length):
        difference = abs(nums1[i] - nums2[i])
        absoluteSum = (absoluteSum + difference) % mod
        j = binarySearch(tempList, nums2[i])
        if j < length:
            maxn = max(maxn, difference - (tempList[j] - nums2[i]))
        if j > 0:
            maxn = max(maxn, difference - (nums2[i] - tempList[j - 1]))
    return (absoluteSum - maxn + mod) % mod


minAbsoluteSumDiffBinarySearch([1, 7, 5], [2, 3, 5])
minAbsoluteSumDiffBinarySearch([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4])
