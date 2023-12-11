# encoding = utf-8
# 477. 汉明距离总和
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
# 计算一个数组中，任意两个数之间汉明距离的总和。
def totalHammingDistance(nums: [int]) -> int:
    length = len(nums)
    if length < 2:
        return 0
    result = 0
    maxLength = len(bin(max(nums))) - 2
    for i in range(length):
        nums[i] = bin(nums[i])[2:].zfill(maxLength)
    for i in range(maxLength):
        oneCounter = 0
        zeroCounter = 0
        for j in range(length):
            if nums[j][i] == '0':
                oneCounter += 1
            else:
                zeroCounter += 1
        result += oneCounter * zeroCounter
    return result


totalHammingDistance([4, 14, 2])
