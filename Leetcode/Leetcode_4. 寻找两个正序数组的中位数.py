# 4. 寻找两个正序数组的中位数
# 给定两个大小为 m 和 n1 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
def findMedianSortedArrays(nums1, nums2):
    nums1 = nums1 + nums2
    nums1.sort()
    if len(nums1) % 2 == 0:
        return float((nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2)
    else:
        return float(nums1[int((len(nums1) - 1) / 2)])


nums1s = [[1, 3], [1, 2], [0, 0], []]
nums2s = [[2], [3, 4], [0, 0], [1]]
for i in range(len(nums1s)):
    print('输入：', nums1s[i], ' 和 ', nums2s[i], '\t结果：', findMedianSortedArrays(nums1s[i], nums2s[i]))
