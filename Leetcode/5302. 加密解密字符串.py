"""
5302. 加密解密字符串
给你一个字符数组 keys ，由若干 互不相同 的字符组成。还有一个字符串数组 values ，内含若干长度为 2 的字符串。
另给你一个字符串数组 dictionary ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 0 开始字符串的数据结构。
字符串 加密 按下述步骤进行：
对字符串中的每个字符 c ，先从 keys 中找出满足 keys[i] == c 的下标 i 。
在字符串中，用 values[i] 替换字符 c 。
字符串 解密 按下述步骤进行：
将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。如果存在多个有效的 i ，
从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。
在字符串中，用 keys[i] 替换 s 。
实现 Encrypter 类：
Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和 dictionary 初始化 Encrypter 类。
String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。
int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。
"""
from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.kvDictionary = {key: value for key, value in zip(keys, values)}
        self.dictionary = set(dictionary)

    def encrypt(self, word1: str) -> str:



    def decrypt(self, word2: str) -> int:

