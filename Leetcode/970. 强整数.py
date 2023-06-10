"""
970. 强整数

给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。
"""
import math
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound <= 1:
            return []
        i_bound = round(math.log(bound - 1, x)) if x != 1 else 1
        j_bound = round(math.log(bound - 1, y)) if y != 1 else 1
        result = set()
        for i in range(i_bound + 1):
            for j in range(j_bound + 1):
                if (temp := x ** i + y ** j) <= bound:
                    result.add(temp)
                else:
                    break
        return list(result)
