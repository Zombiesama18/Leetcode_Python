"""
1031. 两个非重叠子数组的最大和

给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，
长度分别为 firstLen 和 secondLen 。
长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
子数组是数组的一个 连续 部分。
"""
from typing import List
from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))
        sum_a = sum_b = 0
        result = 0
        for i in range(firstLen + secondLen, len(s)):


















            
            sum_a = max(sum_a, s[i - secondLen] - s[i - secondLen - firstLen])
            sum_b = max(sum_b, s[i - firstLen] - s[i - firstLen - secondLen])
            result = max(result, sum_a + s[i] - s[i - secondLen], sum_b + s[i] - s[i - firstLen])
        return result




