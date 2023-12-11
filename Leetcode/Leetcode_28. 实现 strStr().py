# 28. 实现 strStr()
# 实现strStr()函数。
# 给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
# 说明：
# 当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。
def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    targetLength = len(needle)
    hayStackIndex = 0
    tempList = []
    while hayStackIndex < len(haystack):
        tempList.append(haystack[hayStackIndex])
        if len(tempList) == targetLength:
            if ''.join(tempList) == needle:
                return hayStackIndex - targetLength + 1
            tempList.pop(0)
        hayStackIndex += 1
    return -1


haystacks = ['a', "mississippi", "hello", "aaaaa", ""]
needles = ['a', "issip", "ll", "bba", ""]
for i in range(len(haystacks)):
    print('Input: haystack = {}, needle = {} \t Output: {}'.format(haystacks[i], needles[i],
                                                                   strStr(haystacks[i], needles[i])))


def strStrByBulletinFunction(haystack: str, needle: str) -> int:
    return haystack.find(needle)


haystacks = ['a', "mississippi", "hello", "aaaaa", ""]
needles = ['a', "issip", "ll", "bba", ""]
for i in range(len(haystacks)):
    print('Input: haystack = {}, needle = {} \t Output: {}'.format(haystacks[i], needles[i],
                                                                   strStrByBulletinFunction(haystacks[i], needles[i])))
