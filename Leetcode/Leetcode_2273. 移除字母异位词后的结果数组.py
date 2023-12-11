"""
2273. 移除字母异位词后的结果数组
给你一个下标从 0 开始的字符串 words ，其中 words[i] 由小写英文字符组成。
在一步操作中，需要选出任一下标 i ，从 words 中 删除 words[i] 。其中下标 i 需要同时满足下述两个条件：
0 < i < words.length
words[i - 1] 和 words[i] 是 字母异位词 。
只要可以选出满足条件的下标，就一直执行这个操作。
在执行所有操作后，返回 words 。可以证明，按任意顺序为每步操作选择下标都会得到相同的结果。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。例如，"dacb" 是 "abdc" 的一个字母异位词。
"""
from typing import List


def removeAnagrams(words: List[str]) -> List[str]:
    lastWord = ''.join(sorted(words[0]))
    result = [words[0]]
    for i in range(1, len(words)):
        sortedWord = ''.join(sorted(words[i]))
        if sortedWord != lastWord:
            result.append(words[i])
        lastWord = sortedWord
    return result


removeAnagrams(["abba","baba","bbaa","cd","cd"])
