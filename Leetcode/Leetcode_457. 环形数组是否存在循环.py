# 457. 环形数组是否存在循环
# 存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：
# 如果 nums[i] 是正数，向前 移动 nums[i] 步
# 如果 nums[i] 是负数，向后 移动 nums[i] 步
# 因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。
# 数组中的 循环 由长度为 k 的下标序列 seq ：
# 遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# 所有 nums[seq[j]] 应当不是 全正 就是 全负
# k > 1
# 如果 nums 中存在循环，返回 true ；否则，返回 false 。
def circularArrayLoop(nums: [int]) -> bool:
    length = len(nums)

    def dfs(index: int, coveredIndex: int):
        nextIndex = (index + nums[index]) % length
        if nums[index] * nums[nextIndex] < 0:
            return False
        if coveredIndex & (1 << nextIndex) != 0:
            if nextIndex == index:
                return False
            else:
                return True
        coveredIndex |= (1 << nextIndex)
        return dfs(nextIndex, coveredIndex)

    for i in range(length):
        if dfs(i, (1 << i)):
            return True
    return False


circularArrayLoop([2,-1,1,2,2])





