# 78. 子集
# 给定一组不含重复元素的整数数组 nums1，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。


def subsets(nums):
    output = []

    def recursion(start, comb):
        output.append(comb[:])
        for i in range(start, len(nums)):
            recursion(i + 1, comb + [nums[i]])

    recursion(0, [])
    return output


nums = [1, 2, 3]
subsets(nums)
