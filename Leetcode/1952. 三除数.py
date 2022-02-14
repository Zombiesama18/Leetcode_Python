# 1952. 三除数
# 给你一个整数 n 。如果 n 恰好有三个正除数 ，返回 true ；否则，返回 false 。
# 如果存在整数 k ，满足 n = k * m ，那么整数 m 就是 n 的一个 除数 。
def isThree(n: int) -> bool:
    i = 1
    counter = 0
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                counter += 1
            else:
                counter += 2
        if counter > 3:
            return False
        i += 1
    return counter == 3


isThree(4)
