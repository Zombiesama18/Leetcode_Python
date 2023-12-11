"""
1653. 使字符串平衡的最少删除次数

给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。
你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。
请你返回使 s 平衡 的 最少 删除次数。
"""


def minimumDeletions(s: str) -> int:
    left_b, right_a = 0, s.count('a')
    result = right_a
    for char in s:
        if char == 'a':
            right_a -= 1
        else:
            left_b += 1
        result = min(result, left_b + right_a)
    return result


