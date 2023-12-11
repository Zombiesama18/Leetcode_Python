# 461. 汉明距离
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
def hammingDistance(x: int, y: int) -> int:
    binaryX, binaryY = bin(x)[2:], bin(y)[2:]
    length = max(len(binaryX), len(binaryY))
    binaryX = binaryX.zfill(length)
    binaryY = binaryY.zfill(length)
    result = 0
    for i in range(length):
        if binaryX[i] != binaryY[i]:
            result += 1
    return result


hammingDistance(1, 4)


def hammingDistanceByBulletinFunction(x: int, y: int) -> int:
    return bin(x ^ y).count('1')


