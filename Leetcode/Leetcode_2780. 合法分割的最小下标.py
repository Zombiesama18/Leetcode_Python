"""
2780. 合法分割的最小下标
如果元素 x 在长度为 m 的整数数组 arr 中满足 freq(x) * 2 > m ，那么我们称 x 是 支配元素 。
其中 freq(x) 是 x 在数组 arr 中出现的次数。注意，根据这个定义，数组 arr 最多 只会有 一个 支配元素。
给你一个下标从 0 开始长度为 n 的整数数组 nums ，数据保证它含有一个支配元素。
你需要在下标 i 处将 nums 分割成两个数组 nums[0, ..., i] 和 nums[i + 1, ..., n - 1] ，
如果一个分割满足以下条件，我们称它是 合法 的：
0 <= i < n - 1
nums[0, ..., i] 和 nums[i + 1, ..., n - 1] 的支配元素相同。
这里， nums[i, ..., j] 表示 nums 的一个子数组，它开始于下标 i ，结束于下标 j ，
两个端点都包含在子数组内。特别地，如果 j < i ，那么 nums[i, ..., j] 表示一个空数组。
请你返回一个 合法分割 的 最小 下标。如果合法分割不存在，返回 -1 。
"""
import collections
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        number, freqs = counter.most_common(1)[0]
        freq_pre = 0
        for i, num in enumerate(nums):
            freq_pre += num == number
            if freq_pre * 2 > i + 1 and (freqs - freq_pre) * 2 > len(nums) - i - 1:
                return i
        return -1
