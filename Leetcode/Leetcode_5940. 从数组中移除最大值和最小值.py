"""
5940. 从数组中移除最大值和最小值
给你一个下标从 0 开始的数组 nums ，数组由若干 互不相同 的整数组成。
nums 中有一个值最小的元素和一个值最大的元素。分别称为 最小值 和 最大值 。你的目标是从数组中移除这两个元素。
一次 删除 操作定义为从数组的 前面 移除一个元素或从数组的 后面 移除一个元素。
返回将数组中最小值和最大值 都 移除需要的最小删除次数。
"""


def minimumDeletions(nums: [int]) -> int:
    max_num, min_num = float('-INF'), float('INF')
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_index = i
        if nums[i] < min_num:
            min_num = nums[i]
            min_index = i
    if max_index == min_index:
        return 1
    max_num_distance, min_num_distance = min(max_index + 1, len(nums) - max_index), \
                                         min(min_index + 1, len(nums) - min_index)
    relative_distance = abs(max_index - min_index)
    return min(max_num_distance + min_num_distance, max_num_distance + relative_distance,
               min_num_distance + relative_distance)
