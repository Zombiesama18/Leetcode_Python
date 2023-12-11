"""
2186. 使两字符串互为字母异位词的最少步骤数
给你两个字符串 s 和 t 。在一步操作中，你可以给 s 或者 t 追加 任一字符 。
返回使 s 和 t 互为 字母异位词 所需的最少步骤数。
字母异位词 指字母相同但是顺序不同（或者相同）的字符串。
"""
import collections


def minSteps(s: str, t: str) -> int:
    counterS, counterT = collections.Counter(s), collections.Counter(t)
    result = 0
    alphabets = set(counterS.keys()).union(set(counterT.keys()))
    for char in alphabets:
        result += abs(counterS[char] - counterT[char])
    return result
