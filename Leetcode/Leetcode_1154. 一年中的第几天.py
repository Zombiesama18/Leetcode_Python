"""
1154. 一年中的第几天
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。
通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:])
        leapYear = year % 4 == 0
        if leapYear:
            daysInMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(daysInMonth[:month - 1]) + day


