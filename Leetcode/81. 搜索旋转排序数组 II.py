# 81. 搜索旋转排序数组 II
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n1-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。
# 如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
def search(nums: [int], target: int) -> bool:
    return target in nums


# 旋转数组（非有序数组）也能用二分查找，可以发现的是，我们将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。拿示例来看，
# 示例：nums = [4,5,6,7,0,1,2]
# 我们从 6 这个位置分开以后数组变成了 [4, 5, 6] 和 [7, 0, 1, 2] 两个部分，其中左边 [4, 5, 6] 这个部分的数组是有序的，其他也是如此。
# 这启示我们可以在常规二分查找的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，
# 并根据有序的那个部分确定我们该如何改变二分查找的上下界，因为我们能够根据有序的那部分判断出 target 在不在这个部分：
# 如果 [l, mid - 1] 是有序数组，且 target 的大小满足 [nums[l],nums[mid])，
# 则我们应该将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。
# 如果 [mid, r] 是有序数组，且 target 的大小满足 (nums[mid+1],nums[r]]，
# 则我们应该将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
def searchBinarySearch(nums: [int], target: int) -> bool:
    if not nums:
        return False
    length = len(nums)
    if length == 1:
        return target == nums[0]
    left, right = 0, length - 1
    while left <= right:
        mid = left + right >> 1
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] and nums[right] == nums[mid]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


nums = [2,5,6,0,0,1,2]
nums = [5,1,3]
target = 6
searchBinarySearch(nums, target)




