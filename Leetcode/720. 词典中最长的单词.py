"""
720. 词典中最长的单词
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
"""
from typing import List


def longestWord(words: List[str]) -> str:
    def check(word):
        for i in range(1, len(word)):
            if word[:i] not in wordSet:
                return False
        return True

    wordSet = set(words)
    words.sort()
    result = ''
    for word in words:
        if len(word) <= len(result):
            continue
        if check(word) and len(word) > len(result):
            result = word
    return result


longestWord(["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l","o","mwaqz","oi","ych","m","mwa"])
