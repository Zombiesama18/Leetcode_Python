"""
LCP 33. 蓄水

给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：
升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
蓄水：将全部水桶接满水，倒入各自对应的水缸
每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。
注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。
"""
import math
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        num_poor = max(vat)
        if num_poor == 0:
            return 0
        result = float('inf')
        for k in range(1, num_poor + 1):
            temp_result = 0
            for b, v in zip(bucket, vat):
                temp_result += max(0, (v + k - 1) // k - b)
            result = min(result, temp_result + k)
        return result


Solution().storeWater(bucket = [1,3], vat = [6,8])
