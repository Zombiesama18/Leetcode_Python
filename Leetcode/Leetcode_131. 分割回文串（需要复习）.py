# 131. 分割回文串（需要复习）
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
def partition(s: str):
    if not s:
        return []
    result = []

    def backtrack(s, temp, result):
        if not s:
            result.append(temp[:])
            return
        for i in range(1, len(s) + 1):
            if s[: i] == s[i - 1:: -1]:
                temp.append(s[: i])
                backtrack(s[i:], temp, result)
                temp.pop()

    backtrack(s, [], result)
    return result


s = 'aab'
partition(s)
