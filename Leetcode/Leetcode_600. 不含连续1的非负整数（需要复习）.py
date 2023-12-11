# 600. 不含连续1的非负整数（需要复习）
# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。
def findIntegers(n: int) -> int:
    dp = [0] * 31
    dp[0] = 1
    dp[1] = 1
    for i in range(2, 31):
        dp[i] = dp[i - 1] + dp[i - 2]
    pre = 0
    res = 0
    for i in range(29, -1, -1):
        val = (1 << i)
        if n & val:
            n -= val
            res += dp[i + 1]
            if pre == 1:
                break
            pre = 1
        else:
            pre = 0
        if i == 0:
            res += 1
    return res

