# 413. 等差数列划分
# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
# 子数组 是数组中的一个连续序列。
def numberOfArithmeticSlices(nums: [int]) -> int:
    differences = []
    length = len(nums)
    for i in range(1, length):
        differences.append(nums[i] - nums[i - 1])
    counters = []
    counter = 1
    for i in range(1, len(differences)):
        if differences[i] == differences[i - 1]:
            counter += 1
        else:
            counters.append(counter)
            counter = 1
    counters.append(counter)
    result = 0
    for num in counters:
        if num != 1:
            result += int((num - 1) * num / 2)
    return result



