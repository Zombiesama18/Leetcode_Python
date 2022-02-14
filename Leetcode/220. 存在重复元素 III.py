# 220. 存在重复元素 III（需要复习）
# 给你一个整数数组 nums 和两个整数k 和 t 。请你判断是否存在两个下标 i 和 j，使得abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
# 如果存在则返回 true，不存在返回 false。


# 笔记1：范围类型的题可以借助整除来快速归类
# 笔记2：// 和 int() 还不一样，例如 -1 / 2 ， // 为 -1 ，int() 为 0
def containsNearbyAlmostDuplicate(nums: [int], k: int, t: int) -> bool:
    length = len(nums)
    numsWindow = {}
    denominator = t + 1
    for i in range(length):
        inputId = nums[i] // denominator
        if inputId in numsWindow:
            return True
        if inputId + 1 in numsWindow and numsWindow[inputId + 1] - nums[i] < denominator:
            return True
        if inputId - 1 in numsWindow and nums[i] - numsWindow[inputId - 1] < denominator:
            return True
        numsWindow[inputId] = nums[i]
        if i >= k:
            numsWindow.pop((nums[i - k]) // denominator)
    return False


numss = [[2147483647,-1,2147483647], [1,3,6,2],[1,14,23,45,56,2,3], [1,2,3,1], [1,0,1,1], [1,5,9,1,5,9]]
ks = [1, 1, 1, 3, 1, 2]
ts = [2147483647, 2, 10, 0, 2, 3]
for i in range(len(numss)):
    print('输入：nums = {}, k = {}, t = {} \t 结果：{}'.format(numss[i], ks[i], ts[i],
                                                         containsNearbyAlmostDuplicate(numss[i], ks[i], ts[i])))

