"""
1078. Bigram 分词
给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，
third 紧随 second 出现。
对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text = text.split(' ')
        index = 0
        while index < len(text) - 2:
            if text[index] == first and text[index + 1] == second:
                result.append(text[index + 2])
            index += 1
        return result






