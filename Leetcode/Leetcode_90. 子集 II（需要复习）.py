import numpy as np
import datetime
import itertools


# 90. 子集 II（需要复习）
# 给你一个整数数组 nums1 ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
def subsetsWithDupEnumerate(nums: [int]):
    if not nums:
        return [[]]
    result = list()
    length = len(nums)
    nums = sorted(nums)

    def subsetsHelper(subset, counter):
        if subset not in result:
            result.append(subset)
        for i in range(counter, length):
            subsetsHelper(subset + [nums[i]], i + 1)
        return

    subsetsHelper([], 0)
    return result


nums = []
digitNumber = 16
for _ in range(digitNumber):
    nums.append(np.random.randint(0, digitNumber))
startTime = datetime.datetime.now()
# nums1 = [1,2,2]
result1 = subsetsWithDupEnumerate(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)


def subsetsWithDupbyHashCode(nums: [int]):
    if not nums:
        return [[]]
    result = {}
    length = len(nums)
    nums = sorted(nums)

    def subsetsHelper(subset, counter):
        hashCode = hash(tuple(subset))
        if hashCode not in result:
            result[hashCode] = subset
        for i in range(counter, length):
            subsetsHelper(subset + [nums[i]], i + 1)
        return

    subsetsHelper([], 0)
    return list(result.values())


nums = []
digitNumber = 10
for _ in range(digitNumber):
    nums.append(np.random.randint(0, digitNumber))
startTime = datetime.datetime.now()
result2 = subsetsWithDupbyHashCode(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)


def subsetsWithDupbySet(nums: [int]):
    result = []
    length = len(nums)
    nums = sorted(nums)
    temp = set()

    def subsetsHelper(subset, counter):
        temp.add(tuple(subset))
        for i in range(counter, length):
            subsetsHelper(subset + [nums[i]], i + 1)
        return

    subsetsHelper([], 0)
    result.extend(temp)
    return result


result4 = subsetsWithDupbySet(nums)


def subsetsWithDupbyBuiltinFunction(nums: [int]):
    result = [[]]
    nums.sort()
    for i in range(1, len(nums) + 1):
        result.extend(set(itertools.combinations(nums, i)))
    return result


startTime = datetime.datetime.now()
result3 = subsetsWithDupbyBuiltinFunction(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)


def subsetsWithDupbyLogicMethod(nums: [int]):
    temp = list()
    result = list()
    length = len(nums)

    def dfsHelper(choosePre, currentIndex):
        if currentIndex == length:
            result.append(temp.copy())
            return
        dfsHelper(False, currentIndex + 1)
        if (not choosePre) and currentIndex > 0 and nums[currentIndex - 1] == nums[currentIndex]:
            return
        temp.append(nums[currentIndex])
        dfsHelper(True, currentIndex + 1)
        temp.pop(-1)
        return

    nums.sort()
    dfsHelper(False, 0)
    result.sort()
    return result


startTime = datetime.datetime.now()
result5 = subsetsWithDupbyLogicMethod(nums)
endTime = datetime.datetime.now()
print(endTime - startTime)
