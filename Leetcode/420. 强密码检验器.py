"""
420. 强密码检验器
如果一个密码满足下述所有条件，则认为这个密码是强密码：
由至少 6 个，至多 20 个字符组成。
至少包含 一个小写 字母，一个大写 字母，和 一个数字 。
同一字符 不能 连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 如果满足其他条件也可以算是强密码)。
给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0 。
在一步修改操作中，你可以：
插入一个字符到 password ，
从 password 中删除一个字符，或
用另一个字符来替换 password 中的某个字符。
"""


def strongPasswordChecker(password: str) -> int:
    hasLower = hasUpper = hasDigit = False
    for char in password:
        if char.islower():
            hasLower = True
        elif char.isupper():
            hasUpper = True
        elif char.isdigit():
            hasDigit = True
    cases = hasLower + hasUpper + hasDigit
    if len(password) < 6:
        return max(6 - len(password), 3 - cases)
    elif len(password) < 20:
        replaceCounter = counter = 0
        lastChar = ''
        for char in password:
            if char == lastChar:
                counter += 1
            else:
                replaceCounter += counter // 3
                counter = 1
                lastChar = char
        replaceCounter += counter // 3
        return max(replaceCounter, 3 - cases)
    else:
        replaceCounter, removeCounter = 0, len(password) - 20
        removeCounter2 = counter = 0
        lastChar = ''
        for char in password:
            if char == lastChar:
                counter += 1
            else:
                if removeCounter > 0 and counter >= 3:
                    if counter % 3 == 0:
                        removeCounter -= 1
                        replaceCounter -= 1
                    elif counter % 3 == 1:
                        removeCounter2 += 1
                replaceCounter += counter // 3
                counter = 1
                lastChar = char
        if removeCounter > 0 and counter >= 3:
            if counter % 3 == 0:
                removeCounter -= 1
                replaceCounter -= 1
            elif counter % 3 == 1:
                removeCounter2 += 1
        replaceCounter += counter // 3
        useCounter = min(replaceCounter, removeCounter2, removeCounter // 2)
        replaceCounter -= useCounter
        removeCounter -= useCounter * 2
        useCounter2 = min(replaceCounter, removeCounter // 3)
        replaceCounter -= useCounter2
        removeCounter -= useCounter * 3
        return len(password) - 20 + max(replaceCounter, 3 - cases)





