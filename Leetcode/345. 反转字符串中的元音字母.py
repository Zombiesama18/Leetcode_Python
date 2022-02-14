# 345. 反转字符串中的元音字母
# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
def reverseVowels(s: str) -> str:
    vowelSet = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] in vowelSet and s[right] in vowelSet:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        elif s[left] in vowelSet:
            right -= 1
        elif s[right] in vowelSet:
            left += 1
        else:
            right -= 1
            left += 1
    return ''.join(s)

