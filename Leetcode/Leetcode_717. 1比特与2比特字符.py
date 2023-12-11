"""
717. 1比特与2比特字符
有两种特殊字符：
第一种字符可以用一个比特 0 来表示
第二种字符可以用两个比特(10 或 11)来表示、
给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。
"""
from typing import *


def isOneBitCharacter(bits: List[int]) -> bool:
    i = 0
    while i < len(bits):
        if bits[i] == 0 and i == len(bits) - 1:
            return True
        if bits[i] == 0:
            i += 1
        else:
            i += 2
    return False

