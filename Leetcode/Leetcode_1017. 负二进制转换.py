"""
1017. 负二进制转换

给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
"""
import math


def baseNeg2(n: int) -> str:
    number = list(reversed(bin(n)[2:]))
    length = len(number)
    index = 0
    while index < length:
        if number[index] == '1' and index % 2 != 0:
            if index + 1 < length:
                if number[index + 1] == '0':
                    number[index + 1] = '1'
                else:
                    flag = True
                    for i in range(index + 1, length):
                        temp = chr(ord(number[i]) + int(flag))
                        if temp == '2':
                            number[i] = '0'
                            flag = True
                        elif temp == '3':
                            number[i] = '1'
                            flag = True
                        else:
                            flag = False
                            number[i] = temp
                            break
                    if flag:
                        number.append('1')
                        length += 1
            else:
                number.append('1')
                length += 1
        index += 1
    return ''.join(reversed(number))




print(baseNeg2(3))
print(baseNeg2(5))
print(baseNeg2(9))

