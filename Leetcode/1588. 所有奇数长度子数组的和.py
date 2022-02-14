# 1588. 所有奇数长度子数组的和
# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
# 子数组 定义为原数组中的一个连续子序列。
# 请你返回 arr 中 所有奇数长度子数组的和 。
def sumOddLengthSubarrays(arr: [int]) -> int:
    sumOfNItems = [0, arr[0]]
    length = len(arr)
    for i in range(1, length):
        sumOfNItems.append(arr[i] + sumOfNItems[-1])
    result = 0
    for i in range(length, 0, -1):
        counter = 1
        while i - counter >= 0:
            result += sumOfNItems[i] - sumOfNItems[i - counter]
            counter += 2
    return result


sumOddLengthSubarrays([1,4,2,5,3])
