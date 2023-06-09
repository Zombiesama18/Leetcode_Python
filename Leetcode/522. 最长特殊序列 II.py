"""
522. 最长特殊序列 II
给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。
特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 s 的 子序列可以通过删去字符串 s 中的某些字符实现。
例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。
"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
"""
from typing import List


def findLUSlength(strs: List[str]) -> int:

    def is_subseq(string_a, string_b):
        pointer_a = pointer_b = 0
        while pointer_a < len(string_a) and pointer_b < len(string_b):
            if string_a[pointer_a] == string_b[pointer_b]:
                pointer_a += 1
            pointer_b += 1
        return pointer_a == len(string_a)

    result = -1
    for i, string_a in enumerate(strs):
        check = True
        for j, string_b in enumerate(strs):
            if i != j and is_subseq(string_a, string_b):
                check = False
                break
        if check:
            result = max(result, len(string_a))
    return result



