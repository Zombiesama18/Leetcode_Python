# 500. 键盘行
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
# 美式键盘 中：
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
def findWords(words: [str]) -> [str]:
    result = []
    strings = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    stringSets = [set(), set(), set()]
    for i in range(3):
        for char in strings[i]:
            stringSets[i].add(char)

    def isInOneLine(word: str):
        for i in range(3):
            if word[0].lower() in stringSets[i]:
                break
        for j in range(1, len(word)):
            if word[j].lower() not in stringSets[i]:
                return False
        return True

    for word in words:
        if isInOneLine(word):
            result.append(word)
    return result


findWords(["Hello","Alaska","Dad","Peace"])

