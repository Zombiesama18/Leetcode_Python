"""
1446. 连续字符
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串的能量。
"""


def maxPower(s: str) -> int:
    last_char = ''
    counter = 0
    result = 0
    for char in s:
        if char == last_char:
            counter += 1
        else:
            counter = 1
            last_char = char
        result = max(result, counter)
    return result



