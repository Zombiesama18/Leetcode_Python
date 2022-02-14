# 233. 数字 1 的个数
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
def countDigitOne(n: int) -> int:
    stringN = str(n)
    length = len(stringN)
    result = 0
    for i in range(length):
        left = int(stringN[0: i]) if stringN[0: i] else 1
        right = int(stringN[i + 1: -1]) if stringN[i + 1: -1] else 1
        
