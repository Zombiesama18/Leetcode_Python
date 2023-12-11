"""
1518. 换酒问题
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
请你计算 最多 能喝到多少瓶酒。
"""


def numWaterBottles(numBottles: int, numExchange: int) -> int:
    result = numBottles
    new_drink = numBottles // numExchange
    while new_drink != 0:
        new_drink = numBottles // numExchange
        numBottles = new_drink + numBottles % numExchange
        result += new_drink
    return result


numWaterBottles(15, 4)
