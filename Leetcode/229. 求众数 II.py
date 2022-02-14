# 229. 求众数 II
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
import math


def majorityElement(nums: [int]) -> [int]:
    length = len(nums)
    threshold = math.floor(length / 3)
    nums.sort()
    lastNumber = float('INF')
    result = set()
    counter = 0
    for i in range(length):
        if nums[i] == lastNumber:
            counter += 1
        else:
            lastNumber = nums[i]
            counter = 1
        if counter > threshold:
            result.add(nums[i])
    return list(result)


majorityElement([3,2,3])
majorityElement([1])
majorityElement([1,1,1,3,3,2,2,2])


def majorityElementV2(nums: [int]) -> [int]:
    dictionary = {}
    result = []
    threshold = len(nums) // 3
    for num in nums:
        dictionary[num] = dictionary.setdefault(num, 0) + 1
    for key, value in dictionary.items():
        if value > threshold:
            result.append(key)
    return result


majorityElementV2([3,2,3])
majorityElementV2([1])
majorityElementV2([1,1,1,3,3,2,2,2])


