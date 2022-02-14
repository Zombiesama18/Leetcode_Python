# 263. 丑数
# 给你一个整数 n1 ，请你判断 n1 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
# 丑数 就是只包含质因数2、3 和/或5的正整数。
def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    while n != 1:
        if n % 5 == 0:
            n = n / 5
        elif n % 3 == 0:
            n = n / 3
        elif n % 2 == 0:
            n = n / 2
        else:
            return False
    return True


ns = [2 * 3 * 5 * 7, 6, 8, 14, 1, 0]
for n in ns:
    print('输入：', n, '\t', '结果：', isUgly(n))
