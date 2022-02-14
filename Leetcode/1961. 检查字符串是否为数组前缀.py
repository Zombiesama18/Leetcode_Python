# 1961. 检查字符串是否为数组前缀
# 给你一个字符串 s 和一个字符串数组 words ，请你判断 s 是否为 words 的 前缀字符串 。
# 字符串 s 要成为 words 的 前缀字符串 ，需要满足：s 可以由 words 中的前 k（k 为 正数 ）个字符串按顺序相连得到，且 k 不超过 words.length 。
# 如果 s 是 words 的 前缀字符串 ，返回 true ；否则，返回 false 。
def isPrefixString(s: str, words: [str]) -> bool:
    prefixSum = []
    tempString = ''
    for word in words:
        tempString += word
        prefixSum.append(tempString)
    for string in prefixSum:
        if string not in s:
            return False
        if string == s:
            return True
    return False


isPrefixString("iloveleetcode",  ["i","love","leetcode","apples"])
isPrefixString("iloveleetcode", ["apples","i","love","leetcode"])


def isPrefixStringVersion2(s: str, words: [str]) -> bool:
    index = 0
    length = len(s)
    for word in words:
        for char in word:
            if index == length:
                return False
            if char != s[index]:
                return False
            index += 1
        if index == length:
            return True
    return False


isPrefixStringVersion2("iloveleetcode",  ["i","love","leetcode","apples"])
isPrefixStringVersion2("iloveleetcode", ["apples","i","love","leetcode"])

