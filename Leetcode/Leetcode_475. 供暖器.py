"""
475. 供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
在加热器的加热半径范围内的每个房屋都可以获得供暖。
现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
"""
import bisect


def findRadius(houses: [int], heaters: [int]) -> int:
    result = 0
    heaters.sort()
    for house in houses:
        j = bisect.bisect_right(heaters, house)
        i = j - 1
        rightDistance = heaters[j] - house if j < len(heaters) else float('INF')
        leftDistance = house - heaters[i] if j > 0 else float('INF')
        result = max(result, min(rightDistance, leftDistance))
    return result


