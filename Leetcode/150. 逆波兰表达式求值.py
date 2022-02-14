# 150. 逆波兰表达式求值
# 根据 逆波兰表示法，求表达式的值。
# 有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
def evalRPN(tokens):
    if not tokens:
        return 0
    stackNum = list()
    for token in tokens:
        if token.isdigit():
            stackNum.append(int(token))
        elif token[1:].isdigit():
            stackNum.append(int(token))
        elif token == '+':
            stackNum.append(stackNum.pop() + stackNum.pop())
        elif token == '-':
            tempNum = stackNum.pop()
            stackNum.append(stackNum.pop() - tempNum)
        elif token == '*':
            stackNum.append(stackNum.pop() * stackNum.pop())
        elif token == '/':
            tempNum = stackNum.pop()
            stackNum.append(int(stackNum.pop() / tempNum))
    return stackNum[0]


tokens = ["2", "1", "+", "3", "*"]
evalRPN(tokens)
tokens = ["4", "13", "5", "/", "+"]
evalRPN(tokens)
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evalRPN(tokens)


def RPN2NE(tokens):
    stackNum = list()
    for token in tokens:
        if token.isdigit():
            stackNum.append(token)
        elif token[1:].isdigit():
            stackNum.append(token)
        elif token == '+' or token == '-':
            temp = stackNum.pop()
            stackNum.append('(' + stackNum.pop() + token + temp + ')')
        elif token == '*' or token == '/':
            temp = stackNum.pop()
            stackNum.append(stackNum.pop() + token + temp)
    return stackNum[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
RPN2NE(tokens)
