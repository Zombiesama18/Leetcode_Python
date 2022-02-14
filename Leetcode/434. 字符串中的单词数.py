# 434. 字符串中的单词数
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
def countSegments(s: str) -> int:
    spaceFlag = True
    counter = 0
    for char in s:
        if char == ' ':
            if spaceFlag:
                continue
            else:
                spaceFlag = True
        else:
            if spaceFlag:
                counter += 1
                spaceFlag = False
            else:
                continue
    return counter

