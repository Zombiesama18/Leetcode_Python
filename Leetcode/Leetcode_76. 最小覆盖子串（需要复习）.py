# 76. 最小覆盖子串（需要复习）
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n1) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。


# 使用滑动窗口思想，用i,j表示滑动窗口的左边界和右边界，通过改变i,j来扩展和收缩滑动窗口，可以想象成一个窗口在字符串上游走，当这个窗口包含的元素满足条件，即包含字符串T的所有元素，记录下这个滑动窗口的长度j-i+1，这些长度中的最小值就是要求的结果
def minWindow(s, t):
    subsets = []
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            temp = s[i:j]
            if set(t).issubset(set(temp)):
                subsets.append(temp[:])
    length = []
    for i in subsets:
        length.append(len(i))
    return subsets[length.index(min(length))]


s = "ADOBECODEBANC"
t = "ABC"
minWindow(s, t)
