"""
1342. 将数字变成 0 的操作次数
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
"""


def numberOfSteps(num: int) -> int:
    result = 0
    while num:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        result += 1
    return result

