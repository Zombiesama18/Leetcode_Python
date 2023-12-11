"""
917. 仅仅反转字母
给你一个字符串 s ，根据下述规则反转字符串：
所有非英文字母保留在原有位置。
所有英文字母（小写或大写）位置反转。
返回反转后的 s 。
"""


def reverseOnlyLetters(s: str) -> str:
    letters = []
    result = []
    for char in s:
        if char.isalpha():
            result.append('')
            letters.append(char)
        else:
            result.append(char)
    for i in range(len(result)):
        if result[i] == '':
            result[i] = letters.pop(-1)
    return ''.join(result)
