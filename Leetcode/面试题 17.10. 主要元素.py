# 面试题 17.10. 主要元素
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。
# 请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
def majorityElement(nums: [int]) -> int:
    elementDict = {}
    for num in nums:
        elementDict[num] = elementDict.setdefault(num, 0) + 1
    maxElement = max(nums, key=lambda x: elementDict[x])
    if elementDict[maxElement] > (len(nums) / 2):
        return maxElement
    else:
        return -1


