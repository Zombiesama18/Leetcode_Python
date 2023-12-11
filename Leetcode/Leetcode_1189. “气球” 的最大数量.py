"""
1189. “气球” 的最大数量
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
"""
import collections


def maxNumberOfBalloons(text: str) -> int:
    dictionary = collections.Counter(char for char in text if char in 'balon')
    dictionary['l'] //= 2
    dictionary['o'] //= 2
    return min(dictionary.values()) if len(dictionary) == 5 else 0
