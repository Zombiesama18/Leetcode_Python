# 132.分割回文串 II
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 返回符合要求的 最少分割次数 。
import datetime
import random
import string


def minCut_initial(s: str):
    if not s:
        return []
    result = []

    def backtrack(s, temp, result):
        if not s:
            result.append(temp[:])
            return
        for i in range(1, len(s) + 1):
            if s[: i] == s[i - 1:: -1]:
                temp.append(s[: i])
                backtrack(s[i:], temp, result)
                temp.pop()

    backtrack(s, [], result)
    return len(min(result, key=lambda x: len(x))) - 1


letters = string.ascii_letters[5:13]
s = ''
for i in range(50):
    s = s + random.choice(letters)
start_time = datetime.datetime.now()
result1 = minCut_initial(s)
end_time = datetime.datetime.now()
print(end_time - start_time)


def minCut_third(s: str):
    if not s:
        return None
    if len(s) == 1:
        return 0
    length = len(s)
    dp = [float('inf')] * length
    for i in range(length):
        if s[:i + 1] == s[i:: -1]:
            dp[i] = 0
        else:
            for j in range(i):
                if s[j + 1: i + 1] == s[i: j: -1]:
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]


minCut_third(s)
