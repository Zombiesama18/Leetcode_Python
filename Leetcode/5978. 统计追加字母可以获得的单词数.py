"""
5978. 统计追加字母可以获得的单词数
给你两个下标从 0 开始的字符串数组 startWords 和 targetWords 。每个字符串都仅由 小写英文字母 组成。
对于 targetWords 中的每个字符串，检查是否能够从 startWords 中选出一个字符串，执行一次 转换操作 ，得到的结果与当前 targetWords 字符串相等。
转换操作 如下面两步所述：
追加 任何 不存在 于当前字符串的任一小写字母到当前字符串的末尾。
例如，如果字符串为 "abc" ，那么字母 'd'、'e' 或 'y' 都可以加到该字符串末尾，但 'a' 就不行。如果追加的是 'd' ，那么结果字符串为 "abcd" 。
重排 新字符串中的字母，可以按 任意 顺序重新排布字母。
例如，"abcd" 可以重排为 "acbd"、"bacd"、"cbda"，以此类推。注意，它也可以重排为 "abcd" 自身。
找出 targetWords 中有多少字符串能够由 startWords 中的 任一 字符串执行上述转换操作获得。返回 targetWords 中这类 字符串的数目 。
注意：你仅能验证 targetWords 中的字符串是否可以由 startWords 中的某个字符串经执行操作获得。startWords  中的字符串在这一过程中 不 发生实际变更。
"""
import collections
from typing import List


def wordCount(startWords: List[str], targetWords: List[str]) -> int:
    def calculateHash(word):
        hashCode = 0
        for ch in word:
            hashCode = hashCode * 26
            hashCode += ord(ch) - ord('a')
        return hashCode

    dictionary = collections.defaultdict(set)
    for word in startWords:
        dictionary[len(word)].add(calculateHash(sorted(word)))
    result = 0
    for word in targetWords:
        currentCounter = collections.Counter(word)
        if len(word) - 1 not in dictionary:
            continue
        currentWord = sorted(word)
        for i in range(len(word)):
            if currentCounter[currentWord[i]] == 1:
                testWord = currentWord[:i] + currentWord[i + 1:]
                if calculateHash(testWord) in dictionary[len(word) - 1]:
                    result += 1
                    break
    return result


def wordCountVersion2(startWords: List[str], targetWords: List[str]) -> int:
    def toNumber(word: str):
        hashNumber = 0
        for i in range(len(word)):
            hashNumber += 1 << (ord(word[i]) - ord('a'))
        return hashNumber

    wordSet = set()
    for word in startWords:
        wordSet.add(toNumber(word))
    result = 0
    for word in targetWords:
        totalCode = toNumber(word)
        for ch in word:
            if totalCode - (1 << (ord(ch) - ord('a'))) in wordSet:
                result += 1
                break
    return result




