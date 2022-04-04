"""
2212. 射箭比赛中的最大得分
Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下：
Alice 先射 numArrows 支箭，然后 Bob 也射 numArrows 支箭。
分数按下述规则计算：
箭靶有若干整数计分区域，范围从 0 到 11 （含 0 和 11）。
箭靶上每个区域都对应一个得分 k（范围是 0 到 11），Alice 和 Bob 分别在得分 k 区域射中 ak 和 bk 支箭。如果 ak >= bk ，
那么 Alice 得 k 分。如果 ak < bk ，则 Bob 得 k 分
如果 ak == bk == 0 ，那么无人得到 k 分。
例如，Alice 和 Bob 都向计分为 11 的区域射 2 支箭，那么 Alice 得 11 分。如果 Alice 向计分为 11 的区域射 0 支箭，
但 Bob 向同一个区域射 2 支箭，那么 Bob 得 11 分。
给你整数 numArrows 和一个长度为 12 的整数数组 aliceArrows ，该数组表示 Alice 射中 0 到 11 每个计分区域的箭数量。
现在，Bob 想要尽可能 最大化 他所能获得的总分。
返回数组 bobArrows ，该数组表示 Bob 射中 0 到 11 每个 计分区域的箭数量。且 bobArrows 的总和应当等于 numArrows 。
如果存在多种方法都可以使 Bob 获得最大总分，返回其中 任意一种 即可。
"""
from typing import List


def maximumBobPoints(numArrows: int, aliceArrows: List[int]) -> List[int]:
    """
    路径还原 + 0-1 背包
    :param numArrows:
    :param aliceArrows:
    :return:
    """
    dp = [[0 for _ in range(numArrows + 1)] for _ in range(12)]
    result = [0 for _ in range(12)]
    for i in range(1, 12):
        aliceArrow = aliceArrows[i]
        for j in range(1, numArrows):
            if j < aliceArrow:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - aliceArrow - 1] + i, dp[i - 1][j])
    for i in range(11, -1, -1):
        if dp[i][numArrows] > dp[i - 1][numArrows]:
            aliceArrow = aliceArrows[i]
            result[i] = aliceArrow + 1
            numArrows -= aliceArrow + 1
    result[0] = numArrows
    return result


maximumBobPoints(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0])

