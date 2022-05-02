"""
6051. 统计是给定字符串前缀的字符串数目
给你一个字符串数组 words 和一个字符串 s ，其中 words[i] 和 s 只包含 小写英文字母 。
请你返回 words 中是字符串 s 前缀 的 字符串数目 。
一个字符串的 前缀 是出现在字符串开头的子字符串。子字符串 是一个字符串中的连续一段字符序列。
"""
import collections
from typing import List


def countPrefixes(words: List[str], s: str) -> int:
    words = collections.Counter(words)
    result = 0
    for i in range(1, len(s) + 1):
        if s[:i] in words:
            result += words[s[:i]]
    return result

