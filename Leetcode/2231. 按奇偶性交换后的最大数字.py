"""
2231. 按奇偶性交换后的最大数字
给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。
返回交换 任意 次之后 num 的 最大 可能值。
"""


def largestInteger(num: int) -> int:
    odds, evens = [], []
    oddEvenFlags = []
    number = num
    while number != 0:
        remains = number % 10
        if remains % 2 == 0:
            evens.append(remains)
            oddEvenFlags.insert(0, 'even')
        else:
            odds.append(remains)
            oddEvenFlags.insert(0, 'odd')
        number //= 10
    odds.sort(reverse=True)
    evens.sort(reverse=True)
    result = 0
    for flag in oddEvenFlags:
        result *= 10
        if flag == 'even':
            result += evens.pop(0)
        else:
            result += odds.pop(0)
    return result


largestInteger(num = 1234)

