# 541. 反转字符串 II
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
def reverseStr(s: str, k: int) -> str:
    s = list(s)
    length = len(s)
    counter = 0
    result = []
    temp = []
    reverseFlag = True
    for i in range(length):
        counter += 1
        temp.append(s[i])
        if counter == k:
            if reverseFlag:
                temp.reverse()
            result.extend(temp)
            temp = []
            reverseFlag = not reverseFlag
            counter = 0
    if reverseFlag:
        temp.reverse()
    result.extend(temp)
    return ''.join(result)


reverseStr("abcdefg", 2)




