# 583. 两个字符串的删除操作
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
def minDistance(word1: str, word2: str) -> int:
    length1, length2 = len(word1), len(word2)
    dp = [[0 for _ in range(length2)] for _ in range(length1)]
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    maxLength = dp[-1][-1]
    return length1 + length2 - 2 * maxLength

