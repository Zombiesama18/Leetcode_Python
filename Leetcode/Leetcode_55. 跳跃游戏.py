# 55. 跳跃游戏
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。


# 就是看序号加数值能不能大于终点
def canJump(nums):
    dest = nums[-1]
    for i, v in enumerate(nums[0:-1]):
        if i + v >= dest:
            return True
    return False


nums = [3, 2, 1, 0, 4]
canJump(nums)
