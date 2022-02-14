# 301. 删除无效的括号
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
# 返回所有可能的结果。答案可以按 任意顺序 返回。
def removeInvalidParentheses(s: str) -> [str]:
    def isValid(string: str):
        counter = 0
        for char in string:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                if counter < 0:
                    return False
        return counter == 0

    result = []
    currentSet = {s}
    while True:
        for string in currentSet:
            if isValid(string):
                result.append(string)
        if len(result) > 0:
            return result
        nextSet = set()
        for string in currentSet:
            for i in range(len(string)):
                if i > 0 and string[i] == s[i - 1]:
                    continue
                if string[i] == '(' or string[i] == ')':
                    nextSet.add(string[:i] + string[i + 1:])
        currentSet = nextSet
