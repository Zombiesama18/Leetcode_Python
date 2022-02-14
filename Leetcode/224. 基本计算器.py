# 224. 基本计算器
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
# 自制版本无法完成s = '(-3+2)-(-4+2)'操作
def calculate_selfmade(s: str):
    if not s:
        return 0
    stack_num = [0]
    stack_ope = ['+']

    def sub_calc():
        if len(stack_num) == 1:
            number2 = stack_num.pop()
            stack_num.append(0)
            stack_num.append(number2)
        operator = stack_ope[-1]
        if operator == '+':
            number1 = stack_num.pop()
            stack_ope.pop()
            if stack_ope and stack_ope[-1] == '-':
                stack_num[-1] = stack_num[-1] - number1
            else:
                stack_num[-1] = stack_num[-1] + number1
        elif operator == '-':
            number1 = stack_num.pop()
            stack_ope.pop()
            if stack_ope and stack_ope[-1] == '-':
                stack_num[-1] = stack_num[-1] + number1
            else:
                stack_num[-1] = stack_num[-1] - number1
        return

    def digitMerge():
        number1 = stack_num.pop()
        stack_num[-1] = 10 * stack_num[-1] + number1
        return

    temp = ''
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        elif s[i] == '+' or s[i] == '-' or s[i] == '(':
            stack_ope.append(s[i])
        elif s[i] == ')':
            if stack_ope[-1] == '(':
                stack_ope.pop()
                sub_calc()
            else:
                while stack_ope[-1] != '(':
                    sub_calc()
                stack_ope.pop()
        elif s[i].isdigit():
            if temp.isdigit():
                stack_num.append(int(s[i]))
                digitMerge()
            else:
                if i < len(s) - 1 and s[i + 1].isdigit():
                    stack_num.append(int(s[i]))
                else:
                    stack_num.append(int(s[i]))
                    sub_calc()
        temp = s[i]
    while stack_ope:
        sub_calc()
    return stack_num[-1]


s = "1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10"
s = '(-3+2)-(-4+2)'
calculate_selfmade(s)


def calculate_recommonded(s: str):
    stack_ops = [1]
    sign = 1
    result = 0
    length = len(s)
    i = 0
    while i < length:
        if s[i] == ' ':
            i += 1
        elif s[i] == '+':
            sign = stack_ops[-1]
            i += 1
        elif s[i] == '-':
            sign = -stack_ops[-1]
            i += 1
        elif s[i] == '(':
            stack_ops.append(sign)
            i += 1
        elif s[i] == ')':
            stack_ops.pop()
            i += 1
        else:
            num = 0
            while i < length and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            result += num * sign
    return result


s = "1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10"
calculate_recommonded(s)
