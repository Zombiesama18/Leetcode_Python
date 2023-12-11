"""
2209. 用地毯覆盖后的最少白色砖块
给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。
floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。
请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。
请你返回没被覆盖的白色砖块的 最少 数目。
"""
import heapq

"""
用 f[i][j] 表示用 i 条地毯覆盖前 j 块板砖时，没被覆盖的白色砖块的最少数目。
不覆盖：f[i][j] = f[i][j - 1] + [floor[j] = '1']
覆盖：f[i][j] = f[i - 1][j - carpetLen]
取最小值
"""


def minimumWhiteTiles(floor: str, numCarpets: int, carpetLen: int) -> int:
    length = len(floor)
    f = [[0] * length for _ in range(numCarpets + 1)]
    f[0][0] = ord(floor[0]) % 2
    for i in range(1, length):
        f[0][i] = f[0][i - 1] + ord(floor[i]) % 2
    for i in range(1, numCarpets + 1):
        for j in range(carpetLen, length):
            f[i][j] = min(f[i][j - 1] + ord(floor[j]) % 2, f[i - 1][j - carpetLen])
    return f[numCarpets][length - 1]
