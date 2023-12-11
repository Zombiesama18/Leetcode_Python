# 516. 最长回文子序列
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
def longestPalindromeSubseq(s: str) -> int:
    length = len(s)
    dp = [[0] * length for _ in range(length)]
    for i in range(length - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, length):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][length - 1]


