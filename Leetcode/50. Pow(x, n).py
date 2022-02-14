# 50. Pow(x, n1)
# 实现 pow(x, n1) ，即计算 x 的 n1 次幂函数（即，xn）。
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / myPow(x, - n)
    # result = x
    # counter = 1
    # while counter != n1:
    #     if (2 * counter) > n1:
    #         counter = counter + 1
    #         result = result * x
    #     else:
    #         result = result * result
    #         counter = counter * 2
    # return result
    result = 1
    while n != 0:
        if n % 2 == 1:
            result *= x
        n = int(n / 2)
        x *= x
    return result


myPow(2, 10)
