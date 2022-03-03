"""
2185. 统计包含给定前缀的字符串
给你一个字符串数组 words 和一个字符串 pref 。
返回 words 中以 pref 作为 前缀 的字符串的数目。
字符串 s 的 前缀 就是 s 的任一前导连续字符串。
"""
from typing import *


def prefixCount(words: List[str], pref: str) -> int:
    result = 0
    for word in words:
        if word[:len(pref)] == pref:
            result += 1
    return result

