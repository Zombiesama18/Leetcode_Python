# 852. 山脉数组的峰顶索引
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。
def peakIndexInMountainArray(arr: [int]) -> int:
    return arr.index(max(arr))


def peakIndexInMountainArrayByBinarySearch(arr: [int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid - 1] < arr[mid] < arr[mid + 1]:
            left = mid + 1
        elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
            right = mid
        else:
            return mid


