# 1482. 制作 m 束花所需的最少天数（需要复习）
# 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
# 现要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
# 花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。
# 请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。
def minDaysByBinarySearchAndConditionDeterminer(bloomDay: [int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1

    def minDaysHelper(bunchNumber: int, neighborNumber: int, passedDays: int):
        continuousFlowerGroups = 0
        continuousFlowers = 0
        for singleDay in bloomDay:
            if singleDay > passedDays:
                continuousFlowers = 0
            else:
                continuousFlowers += 1
                if continuousFlowers == neighborNumber:
                    continuousFlowerGroups += 1
                    continuousFlowers = 0
        if continuousFlowerGroups >= bunchNumber:
            return True
        else:
            return False

    left, right = min(bloomDay), max(bloomDay)
    while left < right:
        mid = (left + right) // 2
        if minDaysHelper(bunchNumber=m, neighborNumber=k, passedDays=mid):
            right = mid
        else:
            left = mid + 1
    return left


minDaysByBinarySearchAndConditionDeterminer([1, 10, 3, 10, 2], 3, 1)
minDaysByBinarySearchAndConditionDeterminer([1, 10, 3, 10, 2], 3, 2)
minDaysByBinarySearchAndConditionDeterminer([7, 7, 7, 7, 12, 7, 7], 2, 3)
minDaysByBinarySearchAndConditionDeterminer([1000000000, 1000000000], 1, 1)
minDaysByBinarySearchAndConditionDeterminer([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2)

