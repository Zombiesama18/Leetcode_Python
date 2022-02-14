#!/usr/bin/env Python
# coding=utf-8
# 524. 通过删除字母匹配到字典里最长单词
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
def findLongestWord(s: str, dictionary: [str]) -> str:
    def isSubArray(base: str, target: str):
        pointerOfBase = 0
        pointerOfTarget = 0
        while True:
            if base[pointerOfBase] == target[pointerOfTarget]:
                pointerOfBase += 1
                pointerOfTarget += 1
            else:
                pointerOfBase += 1
            if pointerOfTarget == len(target):
                return True
            if pointerOfBase == len(base):
                return False

    dictionary.sort(key=lambda x: (len(x), x))
    maxLength = 0
    result = ''
    for string in dictionary:
        if isSubArray(s, string) and len(string) > maxLength:
            result = string
            maxLength = len(string)
    return result


findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
findLongestWord('abpcplea', ["a","b","c"])
findLongestWord("aaa", ["aaa","aa","a"])
findLongestWord("abce", ["abe","abc"])

