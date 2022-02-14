# 1239. 串联字符串的最大长度
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
# 请返回所有可行解 s 中最长长度。
def maxLength(arr: [str]) -> int:
    masks = []
    for s in arr:
        mask = 0
        for char in s:
            index = ord(char) - ord('a')
            if (mask >> index) & 1:
                mask = 0
                break
            mask |= 1 << index
        if mask > 0:
            masks.append(mask)

    result = 0

    def backtrack(position: int, mask: int):
        if position == len(masks):
            nonlocal result
            result = max(result, bin(mask).count('1'))
            return
        if mask & masks[position] == 0:
            backtrack(position + 1, mask | masks[position])
        backtrack(position + 1, mask)

    backtrack(0, 0)
    return result


maxLength(["cha","r","act","ers"])
