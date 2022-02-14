# 121. 买卖股票的最佳时机
# 给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。

def maxProfit(prices):
    buy_in = min(prices)
    ind = prices.index(buy_in)
    if prices[ind + 1:]:
        return max(prices[ind + 1:]) - buy_in
    else:
        return 0


prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)
prices = [7, 6, 4, 3, 1]
maxProfit(prices)
