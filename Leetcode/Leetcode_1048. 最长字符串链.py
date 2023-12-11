"""
1048. 最长字符串链

给出一个单词数组 words ，其中每个单词都由小写英文字母组成。
如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。
例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。
一个单词通常是 k == 1 的 单词链 。
从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。
"""
import collections
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        len_words_dict = collections.defaultdict(list)
        for word in words:
            len_words_dict[len(word)].append(word)
        dp = [1] * len(words)
        result = 1
        len_words_dict = list(sorted(len_words_dict.items(), key=lambda x: x[0]))
        index = len(len_words_dict[0][1])
        for i in range(1, len(len_words_dict)):
            if len_words_dict[i][0] - len_words_dict[i - 1][0] == 1:
                for j, word2 in enumerate(len_words_dict[i][1]):
                    for k, word1 in enumerate(len_words_dict[i - 1][1]):
                        if self.judge_helper(word1, word2):
                            dp[index + j] = max(dp[index + j], dp[index - len(len_words_dict[i - 1][1]) + k] + 1)
                    result = max(result, dp[index + j])
                index += j + 1
        return result

    def judge_helper(self, word1, word2):
        word1_idx, word2_idx, difference = 0, 0, 0
        while word1_idx < len(word1) and word2_idx < len(word2):
            if word1[word1_idx] == word2[word2_idx]:
                word1_idx += 1
                word2_idx += 1
            elif difference == 1:
                return False
            else:
                difference += 1
                word2_idx += 1
        return True


Solution().longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"])

