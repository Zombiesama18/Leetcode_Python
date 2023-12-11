# coding = utf-8
# 1190. 反转每对括号间的子串
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。
def reverseParenthesesByStack(s: str) -> str:
    if not s:
        return s
    stringStack, temp = [''], ''
    for char in s:
        if char == '(':
            stringStack.append(temp)
            temp = ''
        elif char == ')':
            temp = stringStack.pop() + ''.join(reversed(temp))
        else:
            temp += char
    return temp


reverseParenthesesByStack("(abcd)")
reverseParenthesesByStack("(u(love)i)")
reverseParenthesesByStack("(ed(et(oc))el)")
reverseParenthesesByStack("a(bcdefghijkl(mno)p)q")


