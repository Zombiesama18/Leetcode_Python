# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


# 一般条件判断方法：
# def isValid(s):
#     if not s:
#         return True
#     if s.count('{') != s.count('}') or s.count('[') != s.count(']') or s.count('(') != s.count(')'):
#         return False
#     for i in range(len(s)):
#         if s[i] == '[':
#             if s[i+1] == '{' or s[i+1] == '}' or s[i+1] == ')':
#                 return False
#         if s[i] == '(':
#             if s[i+1] != ')':
#                 return False
#     return True

# 栈方法
def isValid(s):
    stack = []
    str_dict = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in str_dict.keys() and stack and str_dict[i] == stack:
            stack.pop(-1)
        else:
            stack.append(i)
    return not stack


ss = ["({{{{}}}))", "()", "()[]{}", "(]", "{[]}", "([)]"]
for s in ss:
    print('输入：{}\t结果：{}'.format(s, isValid(s)))
