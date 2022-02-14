# 344. 反转字符串
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
# 得到启发：左右指针


# def reverseString(s):
#     left = 0
#     right = len(s) - 1
#     s = list(s)
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#     return ''.join(s)


def reverseString(s):
    s = list(s)
    s.reverse()
    return ''.join(s)


reverseString('hello')
