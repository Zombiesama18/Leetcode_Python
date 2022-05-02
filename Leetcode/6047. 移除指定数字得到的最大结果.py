"""
6047. 移除指定数字得到的最大结果
给你一个表示某个正整数的字符串 number 和一个字符 digit 。
从 number 中 恰好 移除 一个 等于 digit 的字符后，找出并返回按 十进制 表示 最大 的结果字符串。
生成的测试用例满足 digit 在 number 中出现至少一次。
"""


def removeDigit(number: str, digit: str) -> str:
    result = None
    for i in range(len(number)):
        if number[i] == digit:
            temp = number[:i] + number[i + 1:]
            if not result:
                result = temp
            if int(temp) > int(result):
                result = temp
    return result


removeDigit(number = "1231", digit = "1")

