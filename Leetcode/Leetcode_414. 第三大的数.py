# 414. 第三大的数
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
def thirdMax(nums: [int]) -> int:
    first, second, third = float('-INF'), float('-INF'), float('-INF')
    numSet = set()
    for num in nums:
        if num in numSet:
            continue
        numSet.add(num)
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
    if third != float('-INF'):
        return third
    return first




