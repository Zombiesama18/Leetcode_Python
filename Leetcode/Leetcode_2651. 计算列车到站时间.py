"""
2651. 计算列车到站时间

给你一个正整数 arrivalTime 表示列车正点到站的时间（单位：小时），另给你一个正整数 delayedTime 表示列车延误的小时数。
返回列车实际到站的时间。
注意，该问题中的时间采用 24 小时制。
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        delayedTime %= 24
        return (arrivalTime + delayedTime) % 24
