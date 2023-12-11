# 剑指 Offer 38. 字符串的排列
# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
from itertools import permutations


def permutationByItertools(s: str) -> [str]:
    permutationResult = permutations(s)
    result = set()
    for string in permutationResult:
        combinedString = ''.join(string)
        if combinedString not in result:
            result.add(combinedString)
    return list(result)


def permutationBySelfMade(s: str) -> [str]:
    result = set()
    s = list(s)

    def permutationHelper(string: str, length: int, charList: list):
        if length == len(s):
            if string not in result:
                result.add(string)
                return
        for i in range(len(charList)):
            tempList = charList.copy()
            tempChar = tempList.pop(i)
            permutationHelper(string + tempChar, length + 1, tempList)

    permutationHelper('', 0, s)
    return list(result)

