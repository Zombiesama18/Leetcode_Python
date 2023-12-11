# 476. 数字的补数
# 给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。
def findComplement(num: int) -> int:
    highBit = 0
    for i in range(1, 31):
        if num >= (1 << i):
            highBit = i
        else:
            break
    mask = (1 << (highBit + 1)) - 1
    return num ^ mask


findComplement(5)
findComplement(1)

