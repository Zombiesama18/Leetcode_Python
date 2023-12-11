# 115. 不同的子序列（需要复习）
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）
# 题目数据保证答案符合 32 位带符号整数范围。
# 疑问：为什么"rabbb"中"rab"的个数等于"rabb"中"rab"的个数加"rabb"中"ra"的个数
def numDistinct(s: str, t: str):
    if not s or not t or len(t) > len(s):
        return 0
    dp = [[0] * len(s) for _ in range(len(t))]
    dp[0][0] = int(s[0] == t[0])
    for j in range(1, len(s)):
        if s[j] == t[0]:
            dp[0][j] = dp[0][j - 1] + 1
        else:
            dp[0][j] = dp[0][j - 1]
    for i in range(1, len(t)):
        for j in range(len(s)):
            if j < i:
                continue
            if t[i] == s[j]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


s = "rabbbit"
t = "rabbit"
numDistinct(s, t)
s = "babgbag"
t = "bag"
numDistinct(s, t)
