"""
6050. 字符串的总引力
字符串的 引力 定义为：字符串中 不同 字符的数量。
例如，"abbca" 的引力为 3 ，因为其中有 3 个不同字符 'a'、'b' 和 'c' 。
给你一个字符串 s ，返回 其所有子字符串的总引力 。
子字符串 定义为：字符串中的一个连续字符序列。
"""


def appealSum(s: str) -> int:
    result = 0
    summation = 0
    position = [-1] * 26
    for i, char in enumerate(s):
        char = ord(char) - ord('a')
        summation += i - position[char]
        result += summation
        position[char] = i
    return result


appealSum(s = "abbca")
