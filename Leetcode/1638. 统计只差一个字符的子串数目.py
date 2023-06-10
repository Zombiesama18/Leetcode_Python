"""
1638. 统计只差一个字符的子串数目

给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，
请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。
比方说， "computer" and "computation" 只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。
请你返回满足上述条件的不同子字符串对数目。
一个 子字符串 是一个字符串中连续的字符。
"""
import collections


def countSubstrings(s: str, t: str) -> int:

    def traverse(src, span, index):
        if index + span > len(t):
            return 0
        if sum([int(s_char != t_char) for s_char, t_char in zip(src, t[index: index + span])]) == 1:
            return 1 + traverse(src, span, index + 1)
        return 0 + traverse(src, span, index + 1)

    result = 0
    if len(s) > len(t):
        s, t = t, s
    history = dict()

    for i in range(len(s)):
        for j in range(len(s) - i):
            input_src = s[j: j + i + 1]
            if input_src not in history:
                history[input_src] = traverse(input_src, i + 1, 0)
            result += history[input_src]
    return result


countSubstrings(s = "aba", t = "baba")
