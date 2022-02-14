"""
5962. 连接两字母单词得到的最长回文串
给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。
请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。
请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。
回文串 指的是从前往后和从后往前读一样的字符串。
"""
import collections
from typing import List


def longestPalindrome(words: List[str]) -> int:
    singleSelfPlalin = False
    pairs = 0
    wordCounter = collections.Counter(words)
    for word in wordCounter.keys():
        reversedWord = word[1] + word[0]
        if reversedWord in wordCounter:
            if word[0] == word[1]:
                pairs += wordCounter[word] // 2
                singleSelfPlalin = singleSelfPlalin or wordCounter[word] % 2 == 1
                wordCounter[word] = 0
            elif wordCounter[reversedWord] > 0:
                pairs += min(wordCounter[word], wordCounter[reversedWord])
                wordCounter[word] = 0
                wordCounter[reversedWord] = 0
    return 4 * pairs + 2 if singleSelfPlalin else 4 * pairs


longestPalindrome(["lc","cl","gg"])
longestPalindrome(["ab","ty","yt","lc","cl","ab"])
longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"])

