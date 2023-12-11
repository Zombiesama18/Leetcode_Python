"""
765. 情侣牵手

n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。

人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。情侣们按顺序编号，
第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)。
返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。
"""
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos_dict = dict()
        for i in range(0, len(row), 2):
            pos_dict[self.get_couple(row[i])] = i
            pos_dict[self.get_couple(row[i + 1])] = i + 1
        result = 0
        for i in range(0, len(row), 2):
            if row[i] == self.get_couple(row[i + 1]):
                continue
            pos_couple_of_x = pos_dict[row[i]]
            row[pos_couple_of_x] = row[i + 1]
            pos_dict[self.get_couple(row[i + 1])] = pos_couple_of_x
            result += 1
        return result

    def get_couple(self, ids):
        return ids // 2 * 2 + (ids % 2 == 0)


Solution().minSwapsCouples(row = [0,2,1,3])


