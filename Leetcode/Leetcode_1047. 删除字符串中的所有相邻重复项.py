# 1047. 删除字符串中的所有相邻重复项
# 给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
import datetime
import random
import string


def removeDuplicates_first(s: str):
    if len(s) < 2:
        return s
    while True:
        changed = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                changed = True
                break
        if not changed:
            break
    return s


s = "abbaca"
removeDuplicates_first(s)


def removeDuplicates_second(s: str):
    if len(s) < 2:
        return s
    stack = list()
    for i in range(len(s)):
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    return ''.join(stack)


# s = "abbaca"
letters = string.ascii_letters[5:10]
s = ''
for i in range(50000):
    s += random.choice(letters)
start_time = datetime.datetime.now()
result1 = removeDuplicates_first(s)
end_time = datetime.datetime.now()
print(end_time - start_time)
start_time = datetime.datetime.now()
result2 = removeDuplicates_second(s)
end_time = datetime.datetime.now()
print(end_time - start_time)
print(result1 == result2)

