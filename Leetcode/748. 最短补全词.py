"""
748. 最短补全词
给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出并返回 words 中的 最短补全词 。
补全词 是一个包含 licensePlate 中所有的字母的单词。在所有补全词中，最短的那个就是 最短补全词 。
在匹配 licensePlate 中的字母时：
忽略 licensePlate 中的 数字和空格 。
不区分大小写。
如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。
例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。
请你找出并返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 最靠前的 那个。
"""
import collections


def shortestCompletingWord(licensePlate: str, words: [str]) -> str:
    def counter(string):
        temp_dict = collections.defaultdict(int)
        for char in string:
            if char.isalpha():
                temp_dict[char.lower()] += 1
        return temp_dict

    def is_valid(dictionary):
        for char in license_dict:
            if license_dict[char] > dictionary[char]:
                return False
        return True

    result_len, result = float('INF'), ''
    license_dict = counter(licensePlate)
    for word in words:
        word_dict = counter(word)
        if is_valid(word_dict):
            if len(word) < result_len:
                result_len = len(word)
                result = word
    return result


shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])
