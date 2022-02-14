# 96. 不同的二叉搜索树（需要复习）
# 给定一个整数 n1，求以 1 ... n1 为节点组成的二叉搜索树有多少种？
# 假设f(n1)为整数n的二叉搜索树数，而对于一个大于n的数m，有f(m)=f(n1)f(m-n1-1)，即左边是n个元素的二叉搜索树，右边是m-n1-1个元素的二叉搜索树。
# 已知f(0)=1，f(1)=1，对于f(3)，有f(3)=f(0)f(2)+f(1)f(1)+f(2)f(0)，对于每个大于2的整数n都可以细分


def numTrees(n):
    store = [1, 1]
    if n < 2:
        return store[n]
    for m in range(2, n + 1):  # 从2一步一步计算到n
        counter = 0
        for i in range(m):
            counter += store[i] * store[m - 1 - i]
        store.append(counter)
    return store[n]


n = 3
numTrees(n)
