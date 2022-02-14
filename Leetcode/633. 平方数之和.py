# 633. 平方数之和
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
import math


def judgeSquareSumByEnumerating(c: int) -> bool:
    for a in range(int(math.sqrt(c)) + 1):
        if math.sqrt(c - a * a) % 1 == 0:
            return True
    return False


cs = [5, 3, 4, 2, 1]
judgeSquareSumByEnumerating(cs[1])


def judgeSquareSumByDoublePointer(c: int) -> bool:
    a, b = 0, int(math.sqrt(c))
    while a <= b:
        multiplyResult = a * a + b * b
        if multiplyResult == c:
            return True
        if multiplyResult > c:
            b -= 1
        else:
            a += 1
    return False


cs = [5, 3, 4, 2, 1]
result = []
for c in cs:
    result.append(judgeSquareSumByDoublePointer(c))


