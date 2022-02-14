"""
5960. 将标题首字母大写
给你一个字符串 title ，它由单个空格连接一个或多个单词组成，每个单词都只包含英文字母。请你按以下规则将每个单词的首字母 大写 ：
如果单词的长度为 1 或者 2 ，所有字母变成小写。
否则，将单词首字母大写，剩余字母变成小写。
请你返回 大写后 的 title 。
"""


def capitalizeTitle(title: str) -> str:
    return ' '.join([word.capitalize() if len(word) > 2 else word.lower() for word in title.split()])

