"""
556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
"""


def nextGreaterElement(n: int) -> int:
    number = list(str(n))
    i = len(number) - 2
    while i >= 0 and number[i] >= number[i + 1]:
        i -= 1
    if i < 0:
        return -1
    j = len(number) - 1
    while j >= 0 and number[i] >= number[j]:
        j -= 1
    number[i], number[j] = number[j], number[i]
    number[i + 1:] = number[i + 1:][::-1]
    result = int(''.join(number))
    return result if result < 2 ** 31 else -1


nextGreaterElement(230241)


