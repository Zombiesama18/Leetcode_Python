# 46. 全排列
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。


def permute(nums):
    output = []

    def recursion(num):
        if len(num) == len(nums):
            output.append(num.copy())
            return
        for i in nums:
            if i not in num:
                # num.append(i)
                # recursion(num)
                # 不能实现功能，因为num本身也改变了
                recursion(num + [i])

    # 使用（参数+变量）的方式来传递参数
    recursion([])
    return output


nums = [1, 2, 3]
permute(nums)
