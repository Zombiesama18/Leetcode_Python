# 342. 4的幂
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
def isPowerOfFour(n: int) -> bool:
    binary = bin(n)[2:]
    return binary[0] == '1' and len(binary) % 2 == 1 and binary.count('1') == 1


def isPowerOfFourVersion2(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and n & 0xaaaaaaaa == 0
