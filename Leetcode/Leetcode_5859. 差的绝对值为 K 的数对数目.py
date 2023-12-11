# 5859. 差的绝对值为 K 的数对数目
# 给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。
# |x| 的值定义为：
# 如果 x >= 0 ，那么值为 x 。
# 如果 x < 0 ，那么值为 -x 。
def countKDifference(nums: [int], k: int) -> int:
    result = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                result += 1
    return result



