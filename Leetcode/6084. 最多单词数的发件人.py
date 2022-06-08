"""
6084. 最多单词数的发件人
给你一个聊天记录，共包含 n 条信息。给你两个字符串数组 messages 和 senders ，其中 messages[i] 是 senders[i] 发出的一条 信息 。
一条 信息 是若干用单个空格连接的 单词 ，信息开头和结尾不会有多余空格。发件人的 单词计数 是这个发件人总共发出的 单词数 。
注意，一个发件人可能会发出多于一条信息。
请你返回发出单词数 最多 的发件人名字。如果有多个发件人发出最多单词数，请你返回 字典序 最大的名字。
注意：
字典序里，大写字母小于小写字母。
"Alice" 和 "alice" 是不同的名字。
"""
import collections
from typing import List


def largestWordCount(messages: List[str], senders: List[str]) -> str:
    dictionary = collections.defaultdict(int)
    for sender, message in zip(senders, messages):
        dictionary[sender] += len(message.split())
    maxCounter = 0
    result = ''
    for k, v in dictionary.items():
        if v == maxCounter:
            result = max(result, k)
        elif v > maxCounter:
            maxCounter = v
            result = k
    return result
