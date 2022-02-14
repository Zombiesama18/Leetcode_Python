# 88. 合并两个有序数组
# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
# 初始化nums1 和 nums2 的元素数量分别为m 和 n1 。你可以假设nums1 的空间大小等于m + n1，这样它就有足够的空间保存来自 nums2 的元素。
def merge(nums1: [int], m: int, nums2: [int], n: int):
    temp = nums1[0:m]
    counter = 0
    while temp or nums2:
        numFromOne = temp[0] if temp else float('INF')
        numFromTwo = nums2[0] if nums2 else float('INF')
        if numFromTwo > numFromOne:
            nums1[counter] = numFromOne
            temp.pop(0)
        else:
            nums1[counter] = numFromTwo
            nums2.pop(0)
        counter += 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)


def mergeVersion2(nums1: [int], m: int, nums2: [int], n: int):
    lastIndex = m + n - 1
    while n != 0:
        if m == 0 or nums1[m - 1] <= nums2[n - 1]:
            nums1[lastIndex] = nums2[n - 1]
            lastIndex -= 1
            n -= 1
        else:
            nums1[lastIndex] = nums1[m - 1]
            lastIndex -= 1
            m -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
mergeVersion2(nums1, m, nums2, n)
