# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n1 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n1 是一个正整数。


def climbStairs(n):
    def recursion(now, step):
        temp = now + step
        if now + step == n:
            global counter
            counter += 1
            return
        if temp + 2 <= n:
            recursion(temp, 2)
        if temp + 1 <= n:
            recursion(temp, 1)

    if n > 0:
        recursion(0, 1)
    if n > 1:
        recursion(0, 2)
    return


counter = 0
climbStairs(4)
print(counter)
