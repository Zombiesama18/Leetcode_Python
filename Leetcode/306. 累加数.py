"""
306. 累加数
累加数 是一个字符串，组成它的数字可以形成累加序列。
一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
"""


class Solution:
    def valid(self, secondStart: int, secondEnd: int, num: str) -> bool:
        length = len(num)
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd < length:
            third = self.stringAdd(num, firstStart, firstEnd, secondStart, secondEnd)
            thirdStart = secondEnd + 1
            thirdEnd = secondEnd + len(third)
            if thirdEnd >= length or num[thirdStart: thirdEnd + 1] != third:
                break
            if thirdEnd == length - 1:
                return True
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd
        return False

    def stringAdd(self, s: str, firstStart: int, firstEnd: int, secondStart: int, secondEnd: int) -> str:
        third = []
        carry, current = 0, 0
        while firstEnd >= firstStart or secondEnd >= secondStart or carry != 0:
            current = carry
            if firstEnd >= firstStart:
                current += ord(s[firstEnd]) - ord('0')
                firstEnd -= 1
            if secondEnd >= secondStart:
                current += ord(s[secondEnd]) - ord('0')
                secondEnd -= 1
            carry = current // 10
            current %= 10
            third.append(chr(current + ord('0')))
        return ''.join(third[::-1])

    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        for secondStart in range(1, length - 1):
            if num[0] == '0' and secondStart != 1:
                break
            for secondEnd in range(secondStart, length - 1):
                if num[secondStart] == '0' and secondStart != secondEnd:
                    break
                if self.valid(secondStart, secondEnd, num):
                    return True
        return False


def isAdditiveNumber(num):
    def check(secondStart, secondEnd):
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd < length:
            number1 = int(num[firstStart: firstEnd + 1])
            number2 = int(num[secondStart: secondEnd + 1])
            number3 = number1 + number2
            thirdStart = secondEnd + 1
            thirdEnd = thirdStart + len(str(number3)) - 1
            if thirdEnd >= length or int(num[thirdStart: thirdEnd + 1]) != number3:
                break
            if thirdEnd == length - 1:
                return True
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd

    length = len(num)
    for secondBegin in range(1, length - 1):
        if num[0] == '0' and secondBegin != 1:
            break
        for secondOver in range(secondBegin, length - 1):
            if num[secondBegin] == '0' and secondBegin != secondOver:
                break
            if check(secondBegin, secondOver):
                return True
    return False


isAdditiveNumber("112358")
isAdditiveNumber('000')
isAdditiveNumber('1023')
