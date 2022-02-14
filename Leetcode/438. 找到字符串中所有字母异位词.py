"""
438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
"""
import collections


def findAnagrams(s: str, p: str) -> [int]:
    p_dict = collections.Counter(p)
    if len(p) > len(s):
        return []
    result = []
    windows_dict = collections.Counter(s[0: len(p)])
    if windows_dict == p_dict:
        result.append(0)
    for i in range(len(p), len(s)):
        if windows_dict[s[i - len(p)]] == 1:
            del windows_dict[s[i - len(p)]]
        else:
            windows_dict[s[i - len(p)]] -= 1
        windows_dict[s[i]] += 1
        if windows_dict == p_dict:
            result.append(i - len(p) + 1)
    return result



