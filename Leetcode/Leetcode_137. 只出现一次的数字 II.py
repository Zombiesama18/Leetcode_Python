# 137. 只出现一次的数字 II
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
def singleNumber(nums: [int]) -> int:
    numDict = {}
    for num in nums:
        if num not in numDict:
            numDict[num] = 1
        else:
            numDict[num] += 1
    for item in numDict.keys():
        if numDict[item] == 1:
            return item
    return 0


nums = [2,2,3,2]
singleNumber(nums)
nums = [0,1,0,1,0,1,99]
singleNumber(nums)
