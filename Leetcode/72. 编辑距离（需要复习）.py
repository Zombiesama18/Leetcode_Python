# 72. 编辑距离（需要复习）
# 给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符


# 使用动态规划（Dynamic Planining)，dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
# 当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；等于左上角的值，相当于直接把前一个照搬过来。
# 当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，等于上、左上和左的最小值再加一，相当于在之前操作的基础上进行了一步操作。
# 其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。
def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    # 初始化
    for i in range(1, len(word1) + 1):
        dp[i][0] = dp[i - 1][0] + 1
    for j in range(1, len(word2) + 1):
        dp[0][j] = dp[0][j - 1] + 1
    # 进入循环
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:  # dp中的序号比word数组中序号多1
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    print(dp)
    return dp[-1][-1]


word1 = "intention"
word2 = "execution"
minDistance(word1, word2)
