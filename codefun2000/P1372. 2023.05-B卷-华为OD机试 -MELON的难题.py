"""
P1372. 2023.05-B卷-华为OD机试 -MELON的难题

题目描述
MELON有一堆精美的雨花石(数量为n，重量各异)，准备送给S和W。
MELON希望送给俩人的雨花石重量一致，请你设计一个程序，帮
MELON确认是否能将雨花石平均分配。

输入描述
第1行输入为雨花石个数: n, 0<n<31。
第2行输入为空格分割的各雨花石重量:m[0]m[1].....m[n−1]，0<m[k]<1001
不需要考虑异常输入的情况

输出描述
如果可以均分，从当前雨花石中最少拿出几块，可以使两堆的重量相等;如果不能均分，则输出−1。
"""
import collections

n = int(input())
m = list(map(int, input().split()))

summation = sum(m)
if summation % 2 == 0:
    target = summation // 2
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    for i in range(1, target + 1):
        dp[0][i] = n
    for i in range(1, n + 1):
        num = m[i - 1]
        for j in range(1, target + 1):
            if j < num:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - num] + 1)
    if dp[-1][-1] == n:
        print(-1)
    else:
        print(dp[-1][-1])
else:
    print(-1)







