# 5910. 检查两个字符串是否几乎相等
# 如果两个字符串 word1 和 word2 中从 'a' 到 'z' 每一个字母出现频率之差都 不超过 3 ，那么我们称这两个字符串 word1 和 word2 几乎相等 。
# 给你两个长度都为 n 的字符串 word1 和 word2 ，如果 word1 和 word2 几乎相等 ，请你返回 true ，否则返回 false 。
# 一个字母 x 的出现 频率 指的是它在字符串中出现的次数。
import collections


def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    word1_dict = collections.defaultdict(int)
    word2_dict = collections.defaultdict(int)
    for char in word1:
        word1_dict[char] += 1
    for char in word2:
        word2_dict[char] += 1
    for key in word1_dict:
        if abs(word1_dict[key] - word2_dict[key]) > 3:
            return False
    for key in word2_dict:
        if abs(word1_dict[key] - word2_dict[key]) > 3:
            return False
    return True


checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb")
checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc")
checkAlmostEquivalent("zzzyyy", "iiiiii")
