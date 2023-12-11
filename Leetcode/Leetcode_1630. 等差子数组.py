"""
1630. 等差子数组

如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 等差数列 。更正式地，数列 s 是等差数列，
只需要满足：对于每个有效的 i ， s[i+1] - s[i] == s[1] - s[0] 都成立。
例如，下面这些都是 等差数列 ：
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
下面的数列 不是等差数列 ：
1, 1, 2, 5, 7
给你一个由 n 个整数组成的数组 nums，和两个由 m 个整数组成的数组 l 和 r，后两个数组表示 m 组范围查询，
其中第 i 个查询对应范围 [l[i], r[i]] 。所有数组的下标都是 从 0 开始 的。
返回 boolean 元素构成的答案列表 answer 。如果子数组 nums[l[i]], nums[l[i]+1], ... , nums[r[i]] 可以 重新排列 形成 等差数列 ，
answer[i] 的值就是 true；否则answer[i] 的值就是 false 。
"""
from typing import List


def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    def checkArithmetic(arr):
        arr.sort()
        difference = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != difference:
                return False
        return True

    result = []
    for left, right in zip(l, r):
        result.append(checkArithmetic(nums[left: right + 1]))
    return result
