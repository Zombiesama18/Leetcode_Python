"""
2379. 得到 K 个黑块的最少涂色次数

给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，
表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
给你一个整数 k ，表示想要 连续 黑色块的数目。
每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。
"""


from collections import deque


def minimumRecolors(blocks: str, k: int) -> int:
    result = k
    window = deque()
    black_counter = 0
    for i, block in enumerate(blocks):
        if block == 'B':
            black_counter += 1
        window.append(block)
        if len(window) == k + 1:
            item = window.popleft()
            if item == 'B':
                black_counter -= 1
        result = min(result, k - black_counter)
    return result


minimumRecolors("WBBWWBBWBW", 7)

