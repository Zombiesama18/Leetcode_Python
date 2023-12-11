"""
6003. 移除所有载有违禁货物车厢所需的最少时间
给你一个下标从 0 开始的二进制字符串 s ，表示一个列车车厢序列。s[i] = '0' 表示第 i 节车厢 不 含违禁货物，而 s[i] = '1' 表示第 i 节车厢含违禁货物。
作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个：
从列车 左 端移除一节车厢（即移除 s[0]），用去 1 单位时间。
从列车 右 端移除一节车厢（即移除 s[s.length - 1]），用去 1 单位时间。
从列车车厢序列的 任意位置 移除一节车厢，用去 2 单位时间。
返回移除所有载有违禁货物车厢所需要的 最少 单位时间数。
注意，空的列车车厢序列视为没有车厢含违禁货物。
"""


def minimumTime(s: str) -> int:
    length = len(s)
    suffix = [0] * (length + 1)
    for i in range(length - 1, -1, -1):
        suffix[i] = suffix[i + 1] if s[i] == '0' else min(suffix[i + 1] + 2, length - i)
    prefix = 0
    result = suffix[0]
    for i in range(length):
        if s[i] == '1':
            prefix = min(prefix + 2, i + 1)
            result = min(result, prefix + suffix[i + 1])
    return result


