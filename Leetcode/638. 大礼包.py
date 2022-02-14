# 638. 大礼包
# 在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
# 给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中 needs[i] 是需要购买第 i 件物品的数量。
# 还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第 j 件物品的数量，
# 且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。
# 返回 确切 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。
from functools import lru_cache


def shoppingOffers(price: [int], special: [[int]], needs: [int]) -> int:
    length = len(needs)
    filtered_special = []
    for sp in special:
        if sum(sp[i] for i in range(length)) > 0 and sum(sp[i] * price[i] for i in range(length)) > sp[-1]:
            filtered_special.append(sp)

    @lru_cache(None)
    def DFS(currentNeeds):
        minPrice = sum(currentNeeds[i] * price[i] for i in range(length))
        for currentSpecial in filtered_special:
            specialPrice = currentSpecial[-1]
            nextNeeds = []
            for i in range(length):
                if currentSpecial[i] > currentNeeds[i]:
                    break
                nextNeeds.append(currentNeeds[i] - currentSpecial[i])
            if len(nextNeeds) == length:
                minPrice = min(minPrice, DFS(tuple(nextNeeds)) + specialPrice)
        return minPrice

    return DFS(tuple(needs))


