"""
1010. 总持续时间可被 60 整除的歌曲

在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，
我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
"""
import collections
from typing import List
import math


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        divisor_dict = collections.defaultdict(int)
        for t in time:
            divisor_dict[t % 60] += 1
        result = 0
        if divisor_dict[0] > 1:
            result += math.comb(divisor_dict[0], 2)
        del divisor_dict[0]
        if divisor_dict[30] > 1:
            result += math.comb(divisor_dict[30], 2)
        del divisor_dict[30]
        history = set()
        for k, v in divisor_dict.items():
            if k not in history:
                if (60 - k) in divisor_dict:
                    result += divisor_dict[k] * divisor_dict[60 - k]
                    history.add(60 - k)
                history.add(k)
        return result


Solution().numPairsDivisibleBy60([30,20,150,100,40])

