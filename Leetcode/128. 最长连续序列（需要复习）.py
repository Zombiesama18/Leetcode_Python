# 128. 最长连续序列（需要复习）
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n1)。
# 思路一：求出所有序列后算长度
# def longestConsecutive(nums1):
#     nums1.sort()
#     output = []
#     counter = 0
#     flag = True
#     for i in range(1, len(nums1)):
#         if len(output) == counter:
#             output.append([])
#         if nums1[i] == nums1[i - 1] + 1:
#             if flag:
#                 output[counter].append(nums1[i - 1])
#                 output[counter].append(nums1[i])
#                 flag = False
#             else:
#                 output[counter].append(nums1[i])
#         else:
#             flag = True
#             counter += 1
#     lengths = []
#     for i in output:
#         lengths.append(len(i))
#     return max(lengths)
def longestConsecutive(nums):
    nums.sort()
    res = 0
    for num in nums:
        if num - 1 in nums:
            temp = 1
            num = num - 1
            while num + 1 in nums:
                num += 1
                temp += 1
            res = max(res, temp)
    return res


nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)
