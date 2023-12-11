# 312. 戳气球
# 有 n1 个气球，编号为0 到 n1-1，每个气球上都标有一个数字，这些数字存在数组 nums1 中。
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums1[left] * nums1[i] * nums1[right] 个硬币。
# 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 求所能获得硬币的最大数量。
def maxCoins(nums):
    values = []

    def recursion(temp, counter):
        if len(temp) == 2:
            counter += temp[0] * temp[1] + max(temp)
            values.append(counter)
            return
        recursion(temp[1:], counter + temp[0] * temp[1])
        for i in range(1, len(temp) - 1):
            recursion(temp[:i] + temp[i + 1:], counter + (temp[i - 1] * temp[i] * temp[i + 1]))
        recursion(temp[:-1], counter + temp[-2] * temp[-1])

    recursion(nums, 0)
    return max(values)


nums = [3, 1, 5, 8]
maxCoins(nums)

