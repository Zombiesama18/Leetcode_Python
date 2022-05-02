"""
937. 重新排列日志文件
给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。
有两种不同类型的日志：
字母日志：除标识符之外，所有字均由小写字母组成
数字日志：除标识符之外，所有字均由数字组成
请按下述规则将日志重新排序：
所有 字母日志 都排在 数字日志 之前。
字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
数字日志 应该保留原来的相对顺序。
返回日志的最终顺序。
"""
import functools
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    def function(a, b):
        identifierA, identifierB = a.split(' ')[1][0], b.split(' ')[1][0]
        if identifierA.isdigit() and identifierB.isdigit():
            return 0
        elif identifierA.isdigit() and identifierB.isalpha():
            return 1
        elif identifierA.isalpha() and identifierB.isdigit():
            return -1
        else:
            contentA, contentB = ' '.join(a.split(' ')[1:]), ' '.join(b.split(' ')[1:])
            if contentA == contentB:
                return -1 if a.split(' ')[0] < b.split(' ')[0] else 0 if a.split(' ')[0] == b.split(' ')[0] else 1
            else:
                return -1 if contentA < contentB else 0 if contentA == contentB else 1

    return list(sorted(logs, key=functools.cmp_to_key(function)))


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
reorderLogFiles(logs)


def function(a, b):
    identifierA, identifierB = a.split(' ')[1][0], b.split(' ')[1][0]
    if identifierA.isdigit() and identifierB.isdigit():
        return 0
    elif identifierA.isdigit() and identifierB.isalpha():
        return 1
    elif identifierA.isalpha() and identifierB.isdigit():
        return -1
    else:
        contentA, contentB = ' '.join(a.split(' ')[1:]), ' '.join(b.split(' ')[1:])
        if contentA == contentB:
            return -1 if a.split(' ')[0] < b.split(' ')[0] else 0 if a.split(' ')[0] == b.split(' ')[0] else 1
        else:
            return -1 if contentA < contentB else 0 if contentA == contentB else 1


logs = ["let2 own kit dig","let3 art zero"]
reorderLogFiles(logs)

