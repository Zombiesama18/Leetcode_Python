# 10. 正则表达式匹配 （需要复习）
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

# 思路：主要问题是s和p的对齐问题，在p的基础上向s对齐是比较困难的。所以需要另外的状态数组来实现对齐。采取从前传播到后的方法。
# 0代表为空的情况


def isMatch(s, p):
    judge = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
    judge[0][0] = True
    # s和p均为空，结果为True。s为空p非空，若为 字母+* 的格式，也为True。
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*' and judge[0][i - 2]:
            judge[0][i] = True
    # 如果在某个位置上s=p，或p为'.'，则要看之前的状态。
    # 否则如果p='*'，要看前一位，如果前一位不相等且不是'.'，则为False。
    # 如果前一位相等，或为'.'。则要分'*'表示0次，1次和多次前一位。
    # 0次，'a'和'aa*'，当前位状态和两位前相同。
    # 1次，'aa'和'aa*'，当前为状态和前一位相同
    # 多次，'aaa'和'a*'，也是和前一位相同。
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                judge[i][j] = judge[i - 1][j - 1]
            elif p[j - 1] == '*':
                if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                    judge[i][j] = judge[i][j - 2]
                else:
                    judge[i][j] = judge[i][j - 2] or judge[i][j - 1] or judge[i - 1][j]
            else:
                judge[i][j] = False
    return judge[-1][-1]


s = "mississippi"
p = "mis*is*p*."
isMatch(s, p)