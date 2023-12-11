"""
2781. 最长合法子字符串的长度

给你一个字符串 word 和一个字符串数组 forbidden 。
如果一个字符串不包含 forbidden 中的任何字符串，我们称这个字符串是 合法 的。
请你返回字符串 word 的一个 最长合法子字符串 的长度。
子字符串 指的是一个字符串中一段连续的字符，它可以为空。
"""
from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        result = 0
        left, right = 0, 0
        while right < len(word):
            for i in range(right, max(right - 10, left - 1), -1):
                if word[i: right + 1] in forbidden:
                    left = i + 1
                    break
            result = max(result, right - left + 1)
            right += 1
        return result

