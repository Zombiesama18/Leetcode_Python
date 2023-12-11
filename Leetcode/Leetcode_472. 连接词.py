"""
472. 连接词
给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。
"""
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordsSet = set()

        def check(word):
            dp = [-1] * (len(word) + 1)
            dp[0] = 0
            for i in range(len(word) + 1):
                if dp[i] == -1:
                    continue
                temp = ''
                for j in range(i + 1, len(word) + 1):
                    temp += word[j - 1]
                    if temp in wordsSet:
                        dp[j] = max(dp[j], dp[i] + 1)
                    if dp[len(word)] > 1:
                        return True
            return False

        for word in words:
            wordsSet.add(word)
        result = []
        for word in words:
            if check(word):
                result.append(word)
        return result



