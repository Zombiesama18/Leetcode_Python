"""
1576. 替换所有的问号
给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。
注意：你 不能 修改非 '?' 字符。
题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。
在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
"""
import random


def modifyString(s: str) -> str:
    s = [''] + list(s) + ['']
    candidates = [chr(ord('a') + i) for i in range(26)]
    for i in range(1, len(s) - 1):
        if s[i] != '?':
            continue
        while True:
            candidate = random.choice(candidates)
            if s[i - 1] != candidate != s[i + 1]:
                s[i] = candidate
                break
    return ''.join(s[1: -1])


modifyString("??yw?ipkj?")
modifyString("j?qg??b")
modifyString("b?a")
modifyString('?')
