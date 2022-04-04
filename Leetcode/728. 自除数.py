"""
728. 自除数
自除数 是指可以被它包含的每一位数整除的数。
例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
自除数 不允许包含 0 。
给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
"""
from typing import List


def selfDividingNumbers(left: int, right: int) -> List[int]:
    def check(number):
        devider = number % 10
        temp = number
        while temp != 0:
            if devider == 0 or number % devider != 0:
                return False
            temp //= 10
            devider = temp % 10
        return True

    result = []
    for number in range(left, right + 1):
        if check(number):
            result.append(number)
    return result


selfDividingNumbers(left = 1, right = 22)



