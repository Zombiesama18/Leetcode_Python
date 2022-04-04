"""
393. UTF-8 编码验证
给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。
UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：
对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
这是 UTF-8 编码的工作方式：
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
注意：输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。
"""
from typing import List


def validUtf8(data: List[int]) -> bool:
    data = [bin(number)[2:].zfill(8) for number in data]
    index = 0
    while index < len(data):
        if data[index][:3] == '110':
            if index + 1 >= len(data) or data[index + 1][:2] != '10':
                return False
            index += 2
        elif data[index][:4] == '1110':
            if index + 2 >= len(data) or data[index + 1][:2] != '10' or data[index + 2][:2] != '10':
                return False
            index += 3
        elif data[index][:5] == '11110':
            if index + 3 >= len(data) or data[index + 1][:2] != '10' or data[index + 2][:2] != '10' or \
                    data[index + 3][:2] != '10':
                return False
            index += 4
        elif data[index][0] == '0':
            index += 1
        else:
            return False
    return True

