"""
2104. 子数组范围和
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
返回 nums 中 所有 子数组范围的 和 。
子数组是数组中一个连续 非空 的元素序列。
"""
from typing import List


def subArrayRanges(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)):
        maxVal, minVal = float('-inf'), float('inf')
        for j in range(i, len(nums)):
            maxVal = max(nums[j], maxVal)
            minVal = min(nums[j], minVal)
            result += maxVal - minVal
    return result


"""
方法二：单调栈
为了使子数组的最小值或最大值唯一，我们定义如果 nums[i]=nums[j]，那么 nums[i] 与 nums[j] 的逻辑大小由下标 i 与下标 j 的逻辑大小决定，
即如果 i < j，那么 nums[i] 逻辑上小于 nums[j]。
根据范围和的定义，可以推出范围和 sum 等于所有子数组的最大值之和 sumMax 减去所有子数组的最小值之和 sumMin。
假设 nums[i] 左侧最近的比它小的数为 nums[j]，右侧最近的比它小的数为 nums[k]，那么所有以 nums[i] 为最小值的子数组数目为 (k−i)×(i−j)。
为了能获得 nums[i] 左侧和右侧最近的比它小的数的下标，我们可以使用单调递增栈分别预处理出数组 minLeft 和 minRight，
其中 minLeft[i] 表示 nums[i] 左侧最近的比它小的数的下标，minRight[i] 表示 nums[i] 右侧最近的比它小的数的下标。
以求解 minLeft 为例，我们从左到右遍历整个数组 nums。处理到 nums[i] 时，
我们执行出栈操作直到栈为空或者 nums 中以栈顶元素为下标的数逻辑上小于 nums[i]。如果栈为空，那么 minLeft[i]=−1，
否则 minLeft[i] 等于栈顶元素，然后将下标 ii 入栈。
那么所有子数组的最小值之和 sumMin=∑_i=0^n−1 (minRight[i]−i)×(i−minLeft[i])×nums[i]。同理我们也可以求得所有子数组的最大值之和 
sumMax。
"""


def subArrayRangesMonoStack(nums: List[int]) -> int:
    length = len(nums)
    minLeft, maxLeft = [0] * length, [0] * length
    minStack, maxStack = [], []
    for i, num in enumerate(nums):
        while minStack and nums[minStack[-1]] > num:
            minStack.pop()
        minLeft[i] = minStack[-1] if minStack else -1
        minStack.append(i)

        # 如果 nums[maxStack[-1]] == num, 那么根据定义，
        # nums[maxStack[-1]] 逻辑上小于 num，因为 maxStack[-1] < i
        while maxStack and nums[maxStack[-1]] <= num:
            maxStack.pop()
        maxLeft[i] = maxStack[-1] if maxStack else -1
        maxStack.append(i)
    minRight, maxRight = [0] * length, [0] * length
    minStack, maxStack = [], []
    for i in range(length - 1, -1, -1):
        num = nums[i]
        # 如果 nums[minStack[-1]] == num, 那么根据定义，
        # nums[minStack[-1]] 逻辑上大于 num，因为 minStack[-1] > i
        while minStack and nums[minStack[-1]] >= num:
            minStack.pop()
        minRight[i] = minStack[-1] if minStack else length
        minStack.append(i)
        while maxStack and nums[maxStack[-1]] < num:
            maxStack.pop()
        maxRight[i] = maxStack[-1] if maxStack else length
        maxStack.append(i)
    sumMax, sumMin = 0, 0
    for i, num in enumerate(nums):
        sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * num
        sumMin += (minRight[i] - i) * (i - minLeft[i]) * num
    return sumMax - sumMin


subArrayRangesMonoStack([1,2,3])
subArrayRangesMonoStack([4,-2,-3,4,1])

