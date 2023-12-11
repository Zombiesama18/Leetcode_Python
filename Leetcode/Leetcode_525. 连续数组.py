# 525. 连续数组
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
def findMaxLength(nums: [int]) -> int:
    maxLength, counter, lengthDict, length = 0, 0, {0: -1}, len(nums)
    for index in range(length):
        if nums[index] == 1:
            counter += 1
        else:
            counter -= 1
        if counter in lengthDict:
            prevIndex = lengthDict[counter]
            maxLength = max(maxLength, index - prevIndex)
        else:
            lengthDict[counter] = index
    return maxLength


findMaxLength([0,1,1,0,1,1,1,0])
