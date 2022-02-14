# 678. 有效的括号字符串
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。
def checkValidString(s: str) -> bool:
    maxCounter, minCounter = 0, 0
    for char in s:
        if char == '(':
            minCounter += 1
            maxCounter += 1
        if char == ')':
            minCounter = max(minCounter - 1, 0)
            maxCounter -= 1
            if maxCounter < 0:
                return False
        if char == '*':
            minCounter = max(minCounter - 1, 0)
            maxCounter += 1
    return minCounter == 0


checkValidString("()")
checkValidString("(*)")
checkValidString("(*))")




