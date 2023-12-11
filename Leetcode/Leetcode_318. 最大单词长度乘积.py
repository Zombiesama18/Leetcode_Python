"""
318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。
你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
"""
import collections


def maxProduct(words: [str]) -> int:
    word_dicts = []
    for word in words:
        word_dicts.append(collections.Counter(word))

    def have_common_letter(word_dict1, word_dict2):
        for char in word_dict1:
            if char in word_dict2:
                return True
        return False

    result = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if not have_common_letter(word_dicts[i], word_dicts[j]):
                result = max(result, len(words[i]) * len(words[j]))
    return result


maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
maxProduct(["a","ab","abc","d","cd","bcd","abcd"])
maxProduct(["a","aa","aaa","aaaa"])
