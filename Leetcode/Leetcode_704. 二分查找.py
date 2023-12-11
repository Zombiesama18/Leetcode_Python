# 704. 二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，
# 如果目标值存在返回下标，否则返回 -1。
def search(nums: [int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left if nums[left] == target else -1


search([-1,0,3,5,9,12], 9)
search([-1,0,3,5,9,12], 2)
search([-1,0,3,5,9,12], 13)
search([2,5], 5)
