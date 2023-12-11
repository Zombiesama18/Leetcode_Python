# 309. 最佳买卖股票时机含冷冻期
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#     你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#     卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
def maxProfit(prices):
    operation_dict = {0: '按兵不动', 1: '买入', 2: '卖出', 3: '冷冻期'}
    profit_list = []
    history_list = []

    def recursion(day, operation, profit, history, state_buyin):
        if day == len(prices) - 1:
            profit_list.append(profit)
            history_list.append(history[:])
            return
        if operation == 0 or operation == 3:
            if state_buyin:
                recursion(day + 1, 0, profit, history + [0], state_buyin)
                recursion(day + 1, 2, profit + prices[day + 1], history + [2], not state_buyin)
            else:
                recursion(day + 1, 0, profit, history + [0], state_buyin)
                recursion(day + 1, 1, profit - prices[day + 1], history + [1], not state_buyin)
        if operation == 1:
            state_buyin = True
            recursion(day + 1, 0, profit, history + [0], state_buyin)
            recursion(day + 1, 2, profit + prices[day + 1], history + [2], not state_buyin)
        if operation == 2:
            state_buyin = False
            recursion(day + 1, 3, profit, history + [3], state_buyin)

    recursion(0, 0, 0, [0], False)
    recursion(0, 1, -prices[0], [1], True)
    name_list = []
    for i in history_list[profit_list.index(max(profit_list))]:
        name_list.append(operation_dict[i])
    return name_list


prices = [1, 2, 3, 0, 2]
maxProfit(prices)
