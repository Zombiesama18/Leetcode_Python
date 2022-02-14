# 5906. 句子中的有效单词数
# 句子仅由小写字母（'a' 到 'z'）、数字（'0' 到 '9'）、连字符（'-'）、标点符号（'!'、'.' 和 ','）以及空格（' '）组成。
# 每个句子可以根据空格分解成 一个或者多个 token ，这些 token 之间由一个或者多个空格 ' ' 分隔。
# 如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：
# 仅由小写字母、连字符和/或标点（不含数字）。
# 至多一个 连字符 '-' 。如果存在，连字符两侧应当都存在小写字母（"a-b" 是一个有效单词，但 "-ab" 和 "ab-" 不是有效单词）。
# 至多一个 标点符号。如果存在，标点符号应当位于 token 的 末尾 。
# 这里给出几个有效单词的例子："a-b."、"afad"、"ba-c"、"a!" 和 "!" 。
def countValidWords(sentence: str) -> int:
    punctuations = {'!', '.', ','}

    def isValid(word: str):
        hyphenFlag = False
        for i in range(len(word)):
            if word[i].isdigit():
                return False
            elif word[i] == '-':
                if hyphenFlag:
                    return False
                hyphenFlag = True
                if i == 0 or i == len(word) - 1:
                    return False
                if word[i + 1] in punctuations:
                    return False
            elif word[i] in punctuations:
                if i != len(word) - 1:
                    return False
        return True

    words = sentence.split(' ')
    result = 0
    for word in words:
        if word and isValid(word):
            result += 1
    return result


countValidWords("cat and  dog")
countValidWords("!this  1-s b8d!")
countValidWords("alice and  bob are playing stone-game10")
countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.")
countValidWords(" 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex")


