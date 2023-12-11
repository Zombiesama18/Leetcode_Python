"""
(使用java)写一个简易计算器，输入一个expr,输出计算结果
a.  操作符仅支持+ - * 三种
b.  操作数仅支持整数0~9（1位数）,
c.  不支持括号等其它类型，但是要考虑操作符的优先级
d.  不考虑异常情况
int calc(String exprStr) {
   //....
}
样例1： exprStr= "1+2*3"  ,输出7
样例2： exprStr= "2"  ,输出2
样例3： exprStr= "1*2+3*5-6"  ,输出11
"""


def calc(exprStr):
    stack = []
    index = 0
    while index < len(exprStr):
        if exprStr[index].isdigit():
            stack.append(int(exprStr[index]))
            index += 1
        elif exprStr[index] == '*':
            stack.append(stack.pop(-1) * int(exprStr[index + 1]))
            index += 2
        else:
            stack.append(exprStr[index])
            index += 1
    result = stack.pop(-1)
    while stack:
        temp_char = stack.pop(-1)
        if temp_char == '+':
            result += stack.pop(-1)
        else:
            result = stack.pop(-1) - result
    return result


def stack_cal_helper(stack: list):
    if not stack:
        return 0
    temp = stack.pop(-1)
    while stack:
        temp_char = stack.pop(-1)
        if temp_char == '+':
            temp += stack.pop(-1)
        else:
            temp = stack.pop(-1) - temp
    return temp


def calc_v2(exprStr):
    stack = []

    index = 0
    while index < len(exprStr):
        if exprStr[index].isdigit():
            stack.append(int(exprStr[index]))
            index += 1
        elif exprStr[index] == '*':
            stack.append(stack.pop(-1) * int(exprStr[index + 1]))
            index += 2
        else:
            stack = [stack_cal_helper(stack)]
            stack.append(exprStr[index])
            index += 1
    return stack_cal_helper(stack)


if __name__ == '__main__':
    print(calc('1+2*3+4*5-6'))
