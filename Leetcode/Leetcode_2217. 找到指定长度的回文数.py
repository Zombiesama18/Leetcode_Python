"""
2217. 找到指定长度的回文数
给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，
其中 answer[i] 是长度为 intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。
回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。
"""
from typing import List


def kthPalindrome(queries: List[int], intLength: int) -> List[int]:
    base = 10 ** ((intLength - 1) // 2)
    result = [-1] * len(queries)
    for i, query in enumerate(queries):
        if query <= 9 * base:
            leftHalf = str(base + query - 1)
            leftHalf += leftHalf[-2::-1] if intLength % 2 == 1 else leftHalf[::-1]
            result[i] = int(leftHalf)
    return result


kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3)
