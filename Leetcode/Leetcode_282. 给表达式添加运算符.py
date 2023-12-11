#!/usr/bin/env python
# coding=utf-8
# 282. 给表达式添加运算符
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，
# 返回所有能够得到目标值的表达式。


def addOperators(num: str, target: int) -> [str]:
    def DFS(experience: [str], index: int, currentNumber: int, multifiedNumber: int):
        if index == len(num):
            if currentNumber == target:
                result.append(''.join(experience))
            return
        indexOfSign = len(experience)
        if index > 0:
            experience.append(' ')
        thisValue = 0
        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break
            thisValue = thisValue * 10 + int(num[i])
            experience.append(num[i])
            if index == 0:
                DFS(experience, i + 1, thisValue, thisValue)
            else:
                experience[indexOfSign] = '+'
                DFS(experience, index + 1, currentNumber + thisValue, thisValue)
                experience[indexOfSign] = '-'
                DFS(experience, index + 1, currentNumber - thisValue, -thisValue)
                experience[indexOfSign] = '*'
                DFS(experience, index + 1, currentNumber - multifiedNumber + multifiedNumber * thisValue,
                    multifiedNumber * thisValue)
        del experience[indexOfSign:]

    result = []
    DFS([], 0, 0, 0)
    return result


addOperators("123", 6)
addOperators("232", 8)
addOperators("105", 5)
addOperators("00", 0)
addOperators("3456237490", 9191)
