"""
219. 存在重复元素 II
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
如果存在，返回 true ；否则，返回 false 。
"""
import collections


def containsNearbyDuplicate(nums: [int], k: int) -> bool:
    dictionary = collections.defaultdict(int)
    for i in range(len(nums)):
        if i > k:
            dictionary[nums[i - k - 1]] -= 1
        if dictionary[nums[i]] > 0:
            return True
        dictionary[nums[i]] += 1
    return False


def containsNearbyDuplicateSetVersion(nums: [int], k: int) -> bool:
    dictionary = set()
    for i in range(len(nums)):
        if i > k:
            dictionary.discard(nums[i - k - 1])
        if nums[i] in dictionary:
            return True
        dictionary.add(nums[i])
    return False


containsNearbyDuplicate([1,2,3,1,2,3], 2)
