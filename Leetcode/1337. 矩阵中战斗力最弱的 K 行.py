# 1337. 矩阵中战斗力最弱的 K 行
# 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
# 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。
# 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
# 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

def kWeakestRows(mat: [[int]], k: int) -> [int]:
    strength = {}
    counter = 0
    for row in mat:
        strength[counter] = sum(row)
        counter += 1
    result = list(strength.keys())
    result.sort(key=lambda x: strength[x])
    return result[0: k]


kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3)


