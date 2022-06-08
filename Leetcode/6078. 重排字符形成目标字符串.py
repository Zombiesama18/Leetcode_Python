"""
6078. 重排字符形成目标字符串
给你两个下标从 0 开始的字符串 s 和 target 。你可以从 s 取出一些字符并将其重排，得到若干新的字符串。
从 s 中取出字符并重新排列，返回可以形成 target 的 最大 副本数。
"""
import collections


def rearrangeCharacters(s: str, target: str) -> int:
    dictionary = collections.Counter(s)
    targetDict = collections.Counter(target)
    reference = []
    for k, v in targetDict.items():
        reference.append(dictionary[k] // v)
    return min(reference)
