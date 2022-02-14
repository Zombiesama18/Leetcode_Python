# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
def lengthOfLongestSubstringByDict(s):
    subString = dict()
    result = 0
    for i in range(len(s)):
        if s[i] in subString:
            result = max(result, len(subString))
            for char in list(subString.keys()):
                if subString[char] <= subString[s[i]]:
                    subString.pop(char)
                    if char == s[i]:
                        break
        subString[s[i]] = i
    return max(result, len(subString))


ss = ["abcabcbb", "bbbbb", "pwwkew", ""]
for i in range(len(ss)):
    print('输入：', ss[i], '\t结果：', lengthOfLongestSubstringByDict(ss[i]))


def lengthOfLongestSubstringByDictMoreSimple(s):
    subString = dict()
    lastChar = -1
    result = 0
    for index, char in enumerate(s):
        if char in subString and subString[char] > lastChar:
            lastChar = subString[char]
        else:
            result = max(result, index - lastChar)
        subString[char] = index
    return result


ss = ["abcabcbb", "bbbbb", "pwwkew", "", "abcbcde"]
for i in range(len(ss)):
    print('输入：', ss[i], '\t结果：', lengthOfLongestSubstringByDictMoreSimple(ss[i]))
