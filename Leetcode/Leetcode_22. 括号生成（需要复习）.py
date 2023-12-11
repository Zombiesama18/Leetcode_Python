# 22. 括号生成（需要复习）
# 数字 n1 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
def generateParenthesis(n: int):
    result = []

    def generateHelper(combination: str, leftBrace: int, rightBrace: int):
        if leftBrace == 0 and rightBrace == 0:
            result.append(combination)
            return
        if leftBrace > 0:
            generateHelper(combination + '(', leftBrace - 1, rightBrace)
        if leftBrace < rightBrace:
            generateHelper(combination + ')', leftBrace, rightBrace - 1)
        return

    generateHelper('', n, n)
    return result


ns = [3, 1]
for n in ns:
    print('input: n = {},\toutput: {}'.format(n, generateParenthesis(n)))

