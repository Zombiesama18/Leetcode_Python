"""
1185. 一周中的第几天
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
输入为三个整数：day、month 和 year，分别表示日、月、年。
您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
"""
import datetime


def dayOfTheWeek(day: int, month: int, year: int) -> str:
    dictionary = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    return dictionary[(datetime.date(year, month, day) - datetime.date(2022, 1, 2)).days % 7]


def dayOfTheWeekV2(day: int, month: int, year: int) -> str:
    return datetime.datetime(year, month, day).strftime('%A')
