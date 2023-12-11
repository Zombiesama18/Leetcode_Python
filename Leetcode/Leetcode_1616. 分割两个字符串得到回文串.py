"""
1616. 分割两个字符串得到回文串

给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和
asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。
当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc" 那么 "" + "abc" ，
"a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。
注意， x + y 表示连接字符串 x 和 y 。
"""


def checkPalindromeFormation(a: str, b: str) -> bool:

    def checkConcat(s1, s2):
        left, right = 0, len(s1) - 1
        while left < right and s1[left] == s2[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return checkSelfPalidrome(s1, left, right) or checkSelfPalidrome(s2, left, right)

    def checkSelfPalidrome(s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return left >= right

    return checkConcat(a, b) or checkConcat(b, a)
