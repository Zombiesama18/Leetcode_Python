# 1269. 停在原地的方案数
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。
# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
# 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。
# 由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。
def numWays(steps: int, arrLen: int) -> int:
    MODULE = 10**9 + 7
    maxColumn = min(arrLen - 1, steps)
    dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
    dp[0][0] = 1
    for step in range(1, steps + 1):
        for index in range(maxColumn + 1):
            dp[step][index] += dp[step - 1][index] % MODULE
            if index > 0:
                dp[step][index] = (dp[step][index] + dp[step - 1][index - 1]) % MODULE
            if index < maxColumn:
                dp[step][index] = (dp[step][index] + dp[step - 1][index + 1]) % MODULE
    return dp[steps][0]


numWays(3, 2)
numWays(2, 4)
numWays(4, 2)

