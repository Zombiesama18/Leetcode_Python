# 65. 有效数字
# 有效数字（按顺序）可以分成以下几个部分：
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 小数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 部分有效数字列举如下：
# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 部分无效数字列举如下：
# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
def isNumber(s: str) -> bool:
    posNegSign, decimalSign, eSign, digitSign, length = False, False, False, False, len(s)
    posNeg, decimalPoint, e = ['+', '-'], ['.'], ['e', 'E']
    for i in range(len(s)):
        if s[i] in posNeg:
            if posNegSign:
                return False
            posNegSign = True
        elif s[i] in decimalPoint:
            if decimalSign and i == len(s) - 1 or not s[i + 1].isdigit():
                return False
            decimalSign = True
        elif s[i].isalpha():
            if s[i] in e:
                if eSign or not digitSign:
                    return False
                eSign = True
                posNegSign = False
                decimalSign = False
                digitSign = False
            else:
                return False
        elif s[i].isdigit():
            digitSign = True
    return True


isNumber('e')
