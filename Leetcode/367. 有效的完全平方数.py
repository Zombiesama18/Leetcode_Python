# 367. 有效的完全平方数
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 进阶：不要 使用任何内置的库函数，如 sqrt 。
def isPerfectSquare(num: int) -> bool:
    index = 1
    while index * index < num:
        index += 1
    return index * index == num


