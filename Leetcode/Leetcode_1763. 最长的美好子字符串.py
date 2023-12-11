"""
1763. 最长的美好子字符串
当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。比方说，"abABB" 是美好字符串，
因为 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。
给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。
"""


def longestNiceSubstring(s: str) -> str:
    def check(string):
        string = set(string)
        for char in string:
            if char.lower() not in string or char.upper() not in string:
                return False
        return True

    def checkByLength(length):
        index = length
        while index <= len(s):
            if check(s[index - length: index]):
                return s[index - length: index]
            index += 1
        return ''

    result = ''
    for i in range(len(s), 1, -1):
        result = checkByLength(i)
        if result:
            return result
    return result




