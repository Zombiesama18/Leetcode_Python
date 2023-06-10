"""
1147. 段式回文

你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
subtexti 是 非空 字符串
所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
返回k可能最大值。
"""


def longestDecomposition(text: str) -> int:
    left, right = 0, len(text) - 1
    left_side = []
    right_side = []
    result = 0
    while left < right:
        if text[left] == text[right] and not left_side and not right_side:
            result += 2
        else:
            left_side.append(text[left])
            right_side.insert(0, text[right])
            if text[right] == left_side[0]:
                if all([left_side[i] == right_side[i] for i in range(len(left_side))]):
                    left_side = []
                    right_side = []
                    result += 2

        left += 1
        right -= 1
    if left == right:
        left_side.append(text[left])
    if left_side:
        result += 1
    return result


longestDecomposition(text = "ghiabcdefhelloadamhelloabcdefghi")
longestDecomposition("aaa")
