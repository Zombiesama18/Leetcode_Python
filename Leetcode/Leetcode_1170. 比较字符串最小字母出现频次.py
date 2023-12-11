"""
1170. 比较字符串最小字母出现频次

定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，
需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
"""
import bisect
import collections
from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f_words = []
        for word in words:
            temp_dict = collections.Counter(word)
            f_words.append(temp_dict[min(temp_dict.keys())])
        f_words = list(sorted(collections.Counter(f_words).items(), reverse=True))
        f_words_keys = list(reversed([f_word[0] for f_word in f_words]))
        acc_f_words = {f_words[0][0]: f_words[0][1]}
        for i in range(1, len(f_words)):
            acc_f_words[f_words[i][0]] = acc_f_words[f_words[i - 1][0]] + f_words[i][1]
        result = []
        for query in queries:
            temp_dict = collections.Counter(query)
            f_query = temp_dict[min(temp_dict.keys())]
            index = bisect.bisect_left(f_words_keys, f_query + 1)
            if index == len(f_words_keys):
                result.append(0)
            else:
                result.append(acc_f_words[f_words_keys[index]])
        return result


Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])


