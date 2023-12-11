# 451. 根据字符出现频率排序
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
import collections


def frequencySort(s: str) -> str:
    s = list(s)
    sDict = {}
    for char in s:
        if char in sDict:
            sDict[char] += 1
        else:
            sDict[char] = 1
    sDict = list(sDict.items())
    sDict.sort(key=lambda x: x[1], reverse=True)
    result = ''
    for item in sDict:
        result += item[0] * item[1]
    return result



