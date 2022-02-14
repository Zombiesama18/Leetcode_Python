# 58. 最后一个单词的长度
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
def lengthOfLastWord(s: str) -> int:
    splitS = s.split(' ')
    length = len(splitS)
    for i in range(length - 1, -1, -1):
        if splitS[i]:
            return len(splitS[i])


lengthOfLastWord("Hello World")
lengthOfLastWord("   fly me   to   the moon  ")
lengthOfLastWord("luffy is still joyboy")
lengthOfLastWord('a')
