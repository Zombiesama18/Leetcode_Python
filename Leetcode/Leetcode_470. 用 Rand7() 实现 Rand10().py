# 470. 用 Rand7() 实现 Rand10()
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
# 不要使用系统的 Math.random() 方法。
def rand10(self):
    while True:
        row = rand7()
        col = rand7()
        idx = col + (row - 1) * 7
        if idx <= 40:
            break
    return 1 + (idx - 1) % 10
