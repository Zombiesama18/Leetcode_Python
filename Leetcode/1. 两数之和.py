# 1. 两数之和
# 给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
def twoSumByEnumerate(nums, target):
    output = []
    for i in range(0, len(nums)):
        temp = nums[:]
        temp.pop(i)
        if (target - nums[i]) in temp:
            output.append(i)
    return output


def twoSumByHashTable(nums, target):
    hashMap = dict()
    for i in range(0, len(nums)):
        if target - nums[i] in hashMap:
            return [hashMap[target - nums[i]], i]
        hashMap[nums[i]] = i
    return []


numss = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
targets = [9, 6, 6]
for i in range(len(numss)):
    print('输入：nums = ', numss[i], ' target = ', targets[i], '\t结果：', twoSumByHashTable(numss[i], targets[i]))
