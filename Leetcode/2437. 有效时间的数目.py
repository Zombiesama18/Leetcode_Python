"""
2437. 有效时间的数目

给你一个长度为 5 的字符串 time ，表示一个电子时钟当前的时间，格式为 "hh:mm" 。最早 可能的时间是 "00:00" ，最晚 可能的时间是 "23:59" 。
在字符串 time 中，被字符 ? 替换掉的数位是 未知的 ，被替换的数字可能是 0 到 9 中的任何一个。
请你返回一个整数 answer ，将每一个 ? 都用 0 到 9 中一个数字替换后，可以得到的有效时间的数目。
"""


class Solution:
    def countTime(self, time: str) -> int:
        result = 1
        if time[0] == '?':
            if time[1] == '?':
                result = 24
            else:
                if time[1] > '3':
                    result = 2
                else:
                    result = 3
        elif time[1] == '?':
            if time[0] < '2':
                result = 10
            else:
                result = 4
        if time[3] == '?':
            if time[4] == '?':
                result *= 60
            else:
                result *= 6
        elif time[4] == '?':
            result *= 10
        return result
