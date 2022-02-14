# 322. 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。
# 遍历方法
# def coinChange(coins, amount):
#     values = []
#
#     def recursion(history, money):
#         if money == amount:
#             values.append(history[:])
#             return
#         if money > amount:
#             return
#         for i in coins:
#             recursion(history + [i], money + i)
#
#     recursion([], 0)
#     if values:
#         return max(values)
#     else:
#         return -1
# 最大值方法
def coinChange(coins, amount):
    money = 0
    counter = 0
    while money < amount:
        if not coins:
            return -1
        if money + max(coins) > amount:
            coins.remove(max(coins))
        else:
            temp = max(coins)
            money += temp
            counter += 1
    return counter


coins = [1, 2, 5]
amount = 11
coinChange(coins, amount)
