# 171. Excel表列序号
# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 例如，
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
import math


def titleToNumber(columnTitle: str) -> int:
    length, power, result = len(columnTitle), 0, 0
    for i in range(length - 1, -1, -1):
        result += int((ord(columnTitle[i]) - ord('A') + 1) * math.pow(26, power))
        power += 1
    return result


titleToNumber('A')
titleToNumber('AB')
