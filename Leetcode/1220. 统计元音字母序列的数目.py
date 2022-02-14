"""
1220. 统计元音字母序列的数目
给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音 'a' 后面都只能跟着 'e'
每个元音 'e' 后面只能跟着 'a' 或者是 'i'
每个元音 'i' 后面 不能 再跟着另一个 'i'
每个元音 'o' 后面只能跟着 'i' 或者是 'u'
每个元音 'u' 后面只能跟着 'a'
由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
"""


def countVowelPermutation(n: int) -> int:
    MODE = 10**9 + 7
    dp = [[0 for _ in range(5)] for _ in range(n)]
    for i in range(5):
        dp[0][i] = 1
    dictionary = {0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u'}
    for i in range(1, n):
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MODE
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MODE
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MODE
        dp[i][3] = dp[i - 1][2]
        dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MODE
    return sum(dp[-1]) % MODE


countVowelPermutation(5)
