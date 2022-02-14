# 520. 检测大写字母
# 我们定义，在以下情况时，单词的大写用法是正确的：
# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
def detectCapitalUse(word: str) -> bool:
    index = 1
    mode = word[0].isupper()
    while index < len(word):
        if mode:
            if word[index].islower():
                if index == 1:
                    mode = not mode
                else:
                    return False
        else:
            if word[index].isupper():
                return False
        index += 1
    return True


detectCapitalUse('USA')
detectCapitalUse("FlaG")
detectCapitalUse('Google')
