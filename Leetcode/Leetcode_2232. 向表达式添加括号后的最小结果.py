"""
2232. 向表达式添加括号后的最小结果
给你一个下标从 0 开始的字符串 expression ，格式为 "<num1>+<num2>" ，其中 <num1> 和 <num2> 表示正整数。
请你向 expression 中添加一对括号，使得在添加之后， expression 仍然是一个有效的数学表达式，并且计算后可以得到 最小 可能值。
左括号 必须 添加在 '+' 的左侧，而右括号必须添加在 '+' 的右侧。
返回添加一对括号后形成的表达式 expression ，且满足 expression 计算得到 最小 可能值。如果存在多个答案都能产生相同结果，返回任意一个答案。
生成的输入满足：expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围。
"""


def minimizeResult(expression: str) -> str:
    add1, add2 = expression.split('+')
    resultSum = float('INF')
    result = ''
    for i in range(len(add1)):
        for j in range(len(add2)):
            number1 = int(add1[0:i]) if i > 0 else 1
            number2 = int(add1[i:]) + int(add2[:j + 1])
            number3 = int(add2[j + 1:]) if j < len(add2) - 1 else 1
            if number1 * number2 * number3 < resultSum:
                resultSum = number1 * number2 * number3
                result = add1[0:i] + '(' + add1[i:] + '+' + add2[:j + 1] + ')' + add2[j + 1:]
    return result


minimizeResult(expression = "247+38")
