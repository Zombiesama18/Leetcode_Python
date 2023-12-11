# 1486. 数组异或操作
# 给你两个整数，n 和 start 。
# 数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
# 请返回 nums 中所有元素按位异或（XOR）后得到的结果。
def xorOperation(n: int, start: int) -> int:
    if n == 0:
        return 0
    result = start
    for i in range(1, n):
        result = result ^ (start + 2 * i)
    return result


xorOperation(5, 0)
xorOperation(4, 3)
xorOperation(1, 7)
xorOperation(10, 5)
