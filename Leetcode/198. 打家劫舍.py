# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
def rob(nums):
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)
    cashWithDistanceOf2 = nums[0]
    cashWithDistanceOf1 = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        cashWithDistanceOf2, cashWithDistanceOf1 = cashWithDistanceOf1, max(cashWithDistanceOf2 + nums[i], cashWithDistanceOf1)
    return cashWithDistanceOf1


numss = [[2, 7, 9, 3, 1], [1, 2, 3, 1]]
for nums in numss:
    print('输入：{}\t结果：{}'.format(nums, rob(nums)))
