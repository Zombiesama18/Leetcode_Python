# 32. 最长有效括号
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。


def longestValidParentheses(s):
    start = s.index('(')
    left = 0
    counter = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            left += 1
        else:
            left -= 1
            counter += 1
    if left > 0:
        output = counter
    else:
        output = counter - abs(left)
    return 2 * output


s = ")()())"
longestValidParentheses(s)
