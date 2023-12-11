# 523. 连续的子数组和
# 给定一个包含 非负数 的数组和一个目标 整数 k ，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，
# 即总和为 n * k ，其中 n 也是一个整数。
from itertools import accumulate


def checkSubarraySum(nums: [int], k: int) -> bool:
    length = len(nums)
    for num in range(length - 1):
        tempList = list(accumulate(nums[num:]))
        for i in range(1, len(tempList)):
            if tempList[i] % k == 0:
                return True
    return False


checkSubarraySum([23,2,4,6,7], 6)


def checkSubarraySumByPropertyOfRemainder(nums: [int], k: int) -> bool:
    length = len(nums)
    if length < 2:
        return False
    remainderDict, remainder = {0: -1}, 0
    for index in range(length):
        remainder = (remainder + nums[index]) % k
        if remainder in remainderDict:
            if index - remainderDict[remainder] > 1:
                return True
        else:
            remainderDict[remainder] = index
    return False


checkSubarraySumByPropertyOfRemainder([23,2,4,6,7], 6)



