# 5863. 统计特殊四元组
# nums[a] + nums[b] + nums[c] == nums[d] ，且
# a < b < c < d
def countQuadruplets(nums: [int]) -> int:
    length = len(nums)
    result = 0
    for i in range(length - 3):
        for j in range(i + 1, length - 2):
            for k in range(j + 1, length - 1):
                for l in range(k + 1, length):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                        result += 1
    return result


countQuadruplets([1,2,3,6])
