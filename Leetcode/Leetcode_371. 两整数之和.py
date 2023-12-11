# 371. 两整数之和
# 给你两个整数 a 和 b ，不使用 运算符 + 和 - ，计算并返回两整数之和。
def getSum(a: int, b: int) -> int:
    a = bin(a)
    b = bin(b)
    index = -1
    result = ''
    carry = 0
    while a[index] != 'b' and b[index] != 'b':
        result += str(int(a[index]) ^ int(b[index]) ^ carry)
        if
