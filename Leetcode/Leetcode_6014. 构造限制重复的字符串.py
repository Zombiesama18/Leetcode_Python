"""
6014. 构造限制重复的字符串
给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，
使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。
返回 字典序最大的 repeatLimitedString 。
如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。
如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。
"""
import collections


def repeatLimitedString(s: str, repeatLimit: int) -> str:
    dictionary = collections.Counter(s)
    pairs = [list(item) for item in dictionary.items()]
    result = ''
    lastChar = ''
    while len(pairs) > 0:
        pairs.sort(key=lambda x: x[0], reverse=True)
        if pairs[0][0] != lastChar:
            result += pairs[0][0] * min(pairs[0][1], repeatLimit)
            pairs[0][1] -= min(pairs[0][1], repeatLimit)
            lastChar = pairs[0][0]
            if pairs[0][1] == 0:
                pairs.pop(0)
        else:
            if len(pairs) == 1 or pairs[1][1] == 0:
                break
            result += pairs[1][0]
            pairs[1][1] -= 1
            lastChar = pairs[1][0]
            if pairs[1][1] == 0:
                pairs.pop(1)
    return result


repeatLimitedString("cczazcc", 3)
