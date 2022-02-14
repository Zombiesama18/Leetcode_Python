# 453. 最小操作次数使数组元素相等
# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
# 思路：n-1个加1即为剩下那一个减1，计算所有值到最小值的步长和
def minMoves(nums: [int]) -> int:
    minValue = min(nums)
    result = 0
    for num in nums:
        result += num - minValue
    return result

