# 227. 基本计算器 II
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
def calculate_first(s: str):
    length = len(s)
    sign = 1
    index = 0
    stack_num = list()
    stack_ops = list()
    while index < length:
        if s[index] == ' ' or s[index] == '+':
            index = index + 1
        elif s[index] == '-':
            sign = -sign
            index = index + 1
        elif s[index] == '*' or s[index] == '/':
            stack_ops.append(s[index])
            index = index + 1
        else:
            num = 0
            while index < length and s[index].isdigit():
                num = num * 10 + ord(s[index]) - ord('0')
                index = index + 1
            if stack_ops:
                if stack_ops[-1] == '*':
                    stack_num.append(stack_num.pop() * num)
                if stack_ops[-1] == '/':
                    stack_num.append(int(stack_num.pop() / num))
                stack_ops.pop()
            else:
                stack_num.append(sign * num)
                sign = 1
    return sum(stack_num)


s = "3+2*2"
calculate_first(s)
s = " 3/2 "
calculate_first(s)
s = " 3+5 / 2 "
calculate_first(s)
