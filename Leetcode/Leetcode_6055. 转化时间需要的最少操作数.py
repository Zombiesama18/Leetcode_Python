"""
6055. 转化时间需要的最少操作数
给你两个字符串 current 和 correct ，表示两个 24 小时制时间 。
24 小时制时间 按 "HH:MM" 进行格式化，其中 HH 在 00 和 23 之间，而 MM 在 00 和 59 之间。最早的 24 小时制时间为 00:00 ，最晚的是 23:59 。
在一步操作中，你可以将 current 这个时间增加 1、5、15 或 60 分钟。你可以执行这一操作 任意 次数。
返回将  current 转化为 correct 需要的 最少操作数 。
"""


def convertTime(current: str, correct: str) -> int:
    currentHour, currentMinutes = map(int, current.split(':'))
    correctHour, correctMinutes = map(int, correct.split(':'))
    difference = correctMinutes - currentMinutes + (correctHour - currentHour) * 60
    counter = difference // 60
    difference %= 60
    counter += difference // 15
    difference %= 15
    counter += difference // 5
    difference %= 5
    counter += difference // 1
    return counter


convertTime("09:41", "10:34")


