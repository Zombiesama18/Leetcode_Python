# 1968. 构造元素不等于两相邻元素平均值的数组
# 给你一个 下标从 0 开始 的数组 nums ，数组由若干 互不相同的 整数组成。你打算重新排列数组中的元素以满足：重排后，
# 数组中的每个元素都 不等于 其两侧相邻元素的 平均值 。
# 更公式化的说法是，重新排列的数组应当满足这一属性：对于范围    1 <= i < nums.length - 1 中的每个 i ，
# (nums[i-1] + nums[i+1]) / 2 不等于 nums[i] 均成立 。
# 返回满足题意的任一重排结果。
import random


def rearrangeArray(nums: [int]) -> [int]:
    nums.sort()
    result = []
    length = len(nums)
    boundary = (length + 1) // 2
    for i in range(boundary):
        result.append(nums[i])
        if i + boundary < length:
            result.append(nums[i + boundary])
    return result


rearrangeArray([1,2,3,4,5])
rearrangeArray([6,2,0,9,7])


def rearrangeArrayVersion2(nums: [int]) -> [int]:
    length = len(nums)

    def shuffleAndCheck():
        random.shuffle(nums)
        for i in range(1, length - 1):
            if nums[i - 1] + nums[i + 1] == 2 * nums[i]:
                return True
        return False

    while shuffleAndCheck():
        pass
    return nums


rearrangeArrayVersion2([1,2,3,4,5])
rearrangeArrayVersion2([6,2,0,9,7])

