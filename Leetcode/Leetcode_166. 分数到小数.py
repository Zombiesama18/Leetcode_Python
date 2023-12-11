# 166. 分数到小数
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 如果存在多个答案，只需返回 任意一个 。
# 对于所有给定的输入，保证 答案字符串的长度小于 104 。
def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator % denominator == 0:
        return str(numerator // denominator)
    result = ''
    if (numerator < 0) ^ (denominator < 0):
        result += '-'
    if abs(numerator) < abs(denominator):
        result += '0'
    else:
        result += str(abs(numerator) // abs(denominator))
        numerator = abs(numerator) % abs(denominator)
    result += '.'
    denominator = abs(denominator)
    decimalPart = ''
    divisorDict = {}
    index = 0
    while True:
        if 10 * numerator in divisorDict:
            result += '{}({})'.format(decimalPart[0: divisorDict[10 * numerator]],
                                      decimalPart[divisorDict[10 * numerator]:])
            break
        if numerator == 0:
            result += decimalPart
            break
        divisorDict[10 * numerator] = index
        decimalPart += str(10 * numerator // denominator)
        numerator = 10 * numerator % denominator
        index += 1
    return result


fractionToDecimal(1, 2)
fractionToDecimal(2, 1)
fractionToDecimal(2, 3)
fractionToDecimal(4, 333)
fractionToDecimal(1, 5)
fractionToDecimal(666, 7)
fractionToDecimal(1, 6)
fractionToDecimal(50, -8)
fractionToDecimal(7, -12)
fractionToDecimal(-2147483648, 1)
fractionToDecimal(1, 214748364)

