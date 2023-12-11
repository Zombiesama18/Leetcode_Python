# 5869. 两个回文子序列长度的最大乘积
# 给你一个字符串 s ，请你找到 s 中两个 不相交回文子序列 ，使得它们长度的 乘积最大 。两个子序列在原字符串中如果没有任何相同下标的字符，
# 则它们是 不相交 的。
# 请你返回两个回文子序列长度可以达到的 最大乘积 。
# 子序列 指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。
# 如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个 回文字符串 。
import itertools


def maxProduct(s: str) -> int:
    def isPalindrome(string: str):
        return string == string[::-1]

    length = len(s)
    allPalindrome = []
    for i in range(1, 1 << length):
        tempString = ''
        for j in range(length):
            if (1 << j) & i:
                tempString += s[j]
        if isPalindrome(tempString):
            allPalindrome.append(i)
    lengthOfAllPalindrome = len(allPalindrome)
    result = 0
    for i in range(lengthOfAllPalindrome):
        for j in range(i + 1, lengthOfAllPalindrome):
            if not allPalindrome[i] & allPalindrome[j]:
                result = max(result, bin(allPalindrome[i]).count('1') * bin(allPalindrome[j]).count('1'))
    return result


maxProduct("leetcodecom")
maxProduct("bb")


