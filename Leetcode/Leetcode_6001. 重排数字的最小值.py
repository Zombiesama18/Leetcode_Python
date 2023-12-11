"""
6001. 重排数字的最小值
给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。
返回不含前导零且值最小的重排数字。
注意，重排各位数字后，num 的符号不会改变。
"""


def smallestNumber(num: int) -> int:
    negative = False
    result = []
    if num < 0:
        negative = True
    if negative:
        num = list(char for char in str(num)[1:])
        num.sort(reverse=True)
        result = -int(''.join(num))
    else:
        num = list(char for char in str(num))
        num.sort()
        for i in range(len(num)):
            if num[i] != '0':
                result.append(num.pop(i))
                break
        result += num
        result = int(''.join(result))
    return result

