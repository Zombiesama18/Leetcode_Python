# 1833. 雪糕的最大数量
# 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
# 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
# 给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
# 注意：Tony 可以按任意顺序购买雪糕。
def maxIceCream(costs: [int], coins: int) -> int:
    costs.sort()
    length = len(costs)
    if length < 1 or coins < costs[0]:
        return 0
    costsSum = [costs[0]]
    for i in range(1, length):
        costsSum.append(costsSum[-1] + costs[i])
    left, right = 0, length - 1
    while left <= right:
        mid = (left + right) // 2
        if costsSum[mid] >= coins:
            right = mid
        else:
            left = mid + 1
    return left + 1


maxIceCream([1,3,2,4,1], 7)
maxIceCream([1,6,3,1,2,5], 20)
maxIceCream([7,3,3,6,6,6,10,5,9,2], 56)

