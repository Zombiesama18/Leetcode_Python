# 5. 最长回文子串（需要复习）
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
import datetime
import random
import string


def longestPalindrome_selfmade(s):
    result = str()
    lengths = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if i - 1 < 0:
                if s[i: j] == s[j - 1:: -1] and (j - i) > lengths:
                    lengths = j - i
                    result = s[i: j]
            else:
                if s[i: j] == s[j - 1: i - 1: -1] and (j - i) > lengths:
                    lengths = j - i
                    result = s[i: j]
    return result


def longestPalindrome_improved(s):
    if len(s) < 2:
        return s
    length = len(s)
    dp = [[False] * length for _ in range(length)]
    result = ''
    for i in range(length):
        dp[i][i] = True
    for j in range(1, length):
        for i in range(0, j + 1):
            if j == i:
                dp[i][j] = True
            elif j - i == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and j - i + 1 > len(result):
                result = s[i: j + 1]
    return result


letters = string.ascii_letters[5:10]
s = ''
for i in range(1000):
    s = s + random.choice(letters)
start_time = datetime.datetime.now()
longestPalindrome_selfmade(s)
end_time = datetime.datetime.now()
print(end_time - start_time)
start_time = datetime.datetime.now()
longestPalindrome_improved(s)
end_time = datetime.datetime.now()
print(end_time - start_time)