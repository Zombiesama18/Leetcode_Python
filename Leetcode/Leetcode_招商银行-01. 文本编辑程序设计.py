"""
招商银行-01. 文本编辑程序设计
请你设计一个文本编辑程序，需要编辑的稿件 article 为仅由大写字母、小写字母与空格组成的字符串（下标从 0 开始），
光标所在字符串下标位置记作 index，程序运行后，若光标停留位置为空格，不作操作，返回原文本；
否则光标所在位置对应的整个单词将被删除，并返回编辑后经过整理空格的文本。
注意：
输入保证字符串不以空格开头和结尾且不包含连续的空格。
返回的字符串不以空格开头和结尾且不包含连续的空格。若删除单词后有多余的空格，需要删除。
"""


def deleteText(article: str, index: int) -> str:
    if article[index] == ' ':
        return article
    words = []
    counter = 0
    for word in article.split(' '):
        if not counter <= index <= counter + len(word):
            words.append(word)
        counter += len(word) + 1
    return ' '.join(words)


deleteText('hello', 0)
