# 139. 单词拆分
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 说明：
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
def wordBreak(s, wordDict):
    for word in wordDict:
        if word in s:
            s = s.replace(word, '')
        else:
            return False
    if s:
        return False
    else:
        return True


s = "leetcode"
wordDict = ["leet", "code"]
wordBreak(s, wordDict)
s = "applepenapple"
wordDict = ["apple", "pen"]
wordBreak(s, wordDict)
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
wordBreak(s, wordDict)
