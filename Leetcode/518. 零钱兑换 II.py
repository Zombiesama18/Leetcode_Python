# encoding = 'utf-8'
# 518. 零钱兑换 II
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
def changeByTwoDimensionalDynamicPlanning(amount: int, coins: [int]) -> int:
    lengthOfCoins = len(coins)
    dynamicPlanningSpace = [[0] * (lengthOfCoins + 1) for _ in range(amount + 1)]
    for i in range(lengthOfCoins + 1):
        dynamicPlanningSpace[0][i] = 1
    for i in range(1, amount + 1):
        for j in range(1, lengthOfCoins + 1):
            if i >= coins[j - 1]:
                dynamicPlanningSpace[i][j] += dynamicPlanningSpace[i - coins[j - 1]][j]
            dynamicPlanningSpace[i][j] += dynamicPlanningSpace[i][j - 1]
    return dynamicPlanningSpace[-1][-1]


changeByTwoDimensionalDynamicPlanning(5, [1, 2, 5])


def changeByOneDimensionalDynamicPlanning(amount: int, coins: [int]) -> int:
    dynamicPlanningSpace = [0] * (amount + 1)
    dynamicPlanningSpace[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dynamicPlanningSpace[i] += dynamicPlanningSpace[i - coin]
    return dynamicPlanningSpace[-1]


changeByOneDimensionalDynamicPlanning(5, [1, 2, 5])
