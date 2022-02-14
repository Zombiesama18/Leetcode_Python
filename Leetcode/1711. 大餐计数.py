# 1711. 大餐计数（需要复习）
# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
# 你可以搭配 任意 两道餐品做一顿大餐。
# 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。
# 结果需要对 10^9 + 7 取余。
# 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
def countPairs(deliciousness: [int]) -> int:
    MOD = 1000000007
    maxValue = max(deliciousness)
    maxSum = maxValue * 2
    result = 0
    sumDict = {}
    length = len(deliciousness)
    for i in range(length):
        value = deliciousness[i]
        currentSum = 1
        while currentSum <= maxSum:
            count = sumDict.setdefault(currentSum - value, 0)
            result = (result + count) % MOD
            currentSum *= 2
        sumDict[value] = sumDict.setdefault(value, 0) + 1
    return result


countPairs([1,3,5,7,9])


