"""
2274. 不含特殊楼层的最大连续楼层数
Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 特殊楼层 ，仅用于放松。
给你两个整数 bottom 和 top ，表示 Alice 租用了从 bottom 到 top（含 bottom 和 top 在内）的所有楼层。另给你一个整数数组 special ，
其中 special[i] 表示 Alice 指定用于放松的特殊楼层。
返回不含特殊楼层的 最大 连续楼层数。
"""
from typing import List


def maxConsecutive(bottom: int, top: int, special: List[int]) -> int:
    special.sort()
    difference = [special[0] - bottom]
    for i in range(1, len(special)):
        difference.append(special[i] - special[i - 1] - 1)
    return max(max(difference), top - special[-1])



