# 5907. 下一个更大的数值平衡数
# 如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
# 给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
def nextBeautifulNumber(n: int) -> int:
    def isBeautiful(number: int):
        tempDict = dict()
        for num in str(number):
            tempDict[num] = tempDict.setdefault(num, 0) + 1
        for key, value in tempDict.items():
            if int(key) != value:
                del tempDict
                return False
        del tempDict
        return True

    n = n + 1
    while True:
        if isBeautiful(n):
            return n
        n += 1


nextBeautifulNumber(0)
nextBeautifulNumber(1000)
nextBeautifulNumber(3000)



