"""
859. 亲密字符串
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回true；否则返回 false 。
交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
"""


def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    if s == goal:
        if len(set(s)) < len(goal):
            return True
        else:
            return False
    difference = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(difference) == 2 and difference[0][0] == difference[1][1] and difference[0][1] == difference[1][0]


