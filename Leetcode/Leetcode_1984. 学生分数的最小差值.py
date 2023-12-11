# 1984. 学生分数的最小差值
# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
# 返回可能的 最小差值 。
def minimumDifference(nums: [int], k: int) -> int:
    if len(nums) == 1:
        return 0
    nums.sort()
    difference = []
    length = len(nums)
    for i in range(1, length):
        difference.append(nums[i] - nums[i - 1])
    result = sum(difference[: k - 1])
    tempSum = result
    for i in range(k - 1, length - 1):
        tempSum = tempSum + difference[i] - difference[i - k + 1]
        result = min(result, tempSum)
    return result


minimumDifference([9,4,1,7], 2)
minimumDifference([93614,91956,83384,14321,29824,89095,96047,25770,39895], 3)


def minimumDifferenceVersion2(nums: [int], k: int) -> int:
    nums.sort()
    result = float('INF')
    for i in range(k - 1, len(nums)):
        result = min(result, nums[i] - nums[i - k + 1])
    return result


minimumDifferenceVersion2([9,4,1,7], 2)
minimumDifferenceVersion2([93614,91956,83384,14321,29824,89095,96047,25770,39895], 3)
