# 7. 整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
def reverse(x: int) -> int:
    stringForm = str(x)
    if not stringForm[0].isdigit():
        temp = stringForm[1:]
        stringForm = stringForm[0] + ''.join(reversed(temp))
    else:
        stringForm = ''.join(reversed(stringForm))
    return int(stringForm) if -2147483649 < int(stringForm) < 2147483648 else 0
