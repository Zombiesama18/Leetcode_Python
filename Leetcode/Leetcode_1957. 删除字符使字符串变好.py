# 1957. 删除字符使字符串变好
# 一个字符串如果没有 三个连续 相同字符，那么它就是一个 好字符串 。
# 给你一个字符串 s ，请你从 s 删除 最少 的字符，使它变成一个 好字符串 。
# 请你返回删除后的字符串。题目数据保证答案总是 唯一的 。
def makeFancyString(s: str) -> str:
    result = ''
    index = 0
    counter = 0
    lastChar = ''
    length = len(s)
    while index < length:
        if s[index] == lastChar:
            counter += 1
            if counter == 2:
                result += s[index] * 2
        else:
            if counter < 2:
                result += lastChar
            lastChar = s[index]
            counter = 1
        index += 1
    if counter == 1:
        result += lastChar
    return result


makeFancyString("leeetttcode")
makeFancyString("aaabaaaa")
makeFancyString('aab')


def makeFancyStringFaster(s: str) -> str:
    result = []
    for char in s:
        if len(result) > 1 and result[-1] == result[-2] == char:
            continue
        result.append(char)
    return ''.join(result)


