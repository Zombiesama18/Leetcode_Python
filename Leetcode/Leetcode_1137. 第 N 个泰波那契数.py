# 1137. 第 N 个泰波那契数
# 泰波那契序列 Tn 定义如下：
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
def tribonacci(n: int) -> int:
    tNs = [1, 1, 0]
    if n == 0:
        return tNs[2]
    if n == 1:
        return tNs[1]
    counter = 2
    while counter != n:
        tNs.insert(0, sum(tNs))
        tNs.pop(-1)
        counter += 1
    return tNs[0]
