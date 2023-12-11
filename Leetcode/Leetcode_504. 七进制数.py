"""
504. 七进制数
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
"""


def convertToBase7(num: int) -> str:
    if num == 0:
        return '0'
    if num < 0:
        result = '-'
        num = -num
    else:
        result = ''
    while num != 0:
        result += str(num % 7)
        num //= 7
    return ''.join(reversed(result)) if result[0] != '-' else '-' + ''.join(reversed(result[1:]))
