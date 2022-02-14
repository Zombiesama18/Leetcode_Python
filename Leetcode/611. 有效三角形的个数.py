# 611. 有效三角形的个数
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
def triangleNumber(nums: [int]) -> int:
    nums.sort()
    length = len(nums)
    result = 0
    for i in range(length):
        for j in range(i + 1, length):
            left, right, k = j + 1, length - 1, j
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < nums[i] + nums[j]:
                    k = mid
                    left = mid + 1
                else:
                    right = mid - 1
            result += k - j
    return result



