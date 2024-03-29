# 496. 下一个更大元素 I
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
# 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
def nextGreaterElement(nums1: [int], nums2: [int]) -> [int]:
    result = {}
    stack = []
    for num in reversed(nums2):
        while stack and num >= stack[-1]:
            stack.pop()
        result[num] = stack[-1] if stack else -1
        stack.append(num)
    return [result[num] for num in nums1]


nextGreaterElement([4,1,2], [1,3,4,2])
nextGreaterElement([2,4], [1,2,3,4])

