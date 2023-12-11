"""
2409. 统计共同度过的日子数

Alice 和 Bob 计划分别去罗马开会。
给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice
到 leaveAlice 之间在城市里（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。
每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。
请你返回 Alice和 Bob 同时在罗马的天数。
你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：
[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。
"""
import itertools


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.prefix_sum = list(itertools.accumulate(days, initial=0))
        arriveAliceDay = self.calculatedDatofYear(arriveAlice)
        arriveBobDay = self.calculatedDatofYear(arriveBob)
        leaveAliceDay = self.calculatedDatofYear(leaveAlice)
        leaveBobDay = self.calculatedDatofYear(leaveBob)
        return max(0, min(leaveAliceDay, leaveBobDay) - max(arriveAliceDay, arriveBobDay) + 1)

    def calculatedDatofYear(self, day: str):
        return self.prefix_sum[int(day[:2]) - 1] + int(day[3:])
