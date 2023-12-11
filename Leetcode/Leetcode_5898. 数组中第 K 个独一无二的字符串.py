# 5898. 数组中第 K 个独一无二的字符串
# 独一无二的字符串 指的是在一个数组中只出现过 一次 的字符串。
# 给你一个字符串数组 arr 和一个整数 k ，请你返回 arr 中第 k 个 独一无二的字符串 。如果 少于 k 个独一无二的字符串，那么返回 空字符串 "" 。
# 注意，按照字符串在原数组中的 顺序 找到第 k 个独一无二字符串。
import collections


def kthDistinct(arr: [str], k: int) -> str:
    stringDict = collections.OrderedDict()
    for string in arr:
        stringDict[string] = stringDict.setdefault(string, 0) + 1
    for string in stringDict:
        if stringDict[string] == 1:
            if k == 1:
                return string
            k -= 1
    return ''


kthDistinct(["d","b","c","b","c","a"], 2)
kthDistinct(["aaa","aa","a"], 1)
kthDistinct(["a","b","a"], 3)

