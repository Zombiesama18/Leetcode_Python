"""
5956. 找出数组中的第一个回文字符串
给你一个字符串数组 words ，找出并返回数组中的 第一个回文字符串 。如果不存在满足要求的字符串，返回一个 空字符串 "" 。
回文字符串 的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个 回文字符串 。
"""
from typing import List


def firstPalindrome(words: List[str]) -> str:
    def is_palindrome(string):
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    for word in words:
        if is_palindrome(word):
            return word
    return ''



