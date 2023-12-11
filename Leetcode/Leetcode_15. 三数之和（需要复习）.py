# 15. 三数之和（需要复习）
# 给你一个包含 n1 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
def threeSum(nums):
    result = []
    if len(nums) < 3:
        return result
    nums.sort()
    numsDict = dict()
    for num in nums:
        if num in numsDict:
            numsDict[num] += 1
        else:
            numsDict[num] = 1
    for i in range(len(nums) - 2):
        temp = numsDict.copy()
        for index in range(i + 1):
            if temp[nums[index]] == 1:
                temp.pop(nums[index])
            else:
                temp[nums[index]] -= 1
        for j in range(i + 1, len(nums) - 1):
            if temp[nums[j]] == 1:
                temp.pop(nums[j])
            else:
                temp[nums[j]] -= 1
            if -(nums[i] + nums[j]) in temp:
                if [nums[i], nums[j], -(nums[i] + nums[j])] not in result:
                    result.append([nums[i], nums[j], -(nums[i] + nums[j])])
    return result


numss = [[-1, 0, 1, 2, -1, -4], [], [0]]
for i in range(len(numss)):
    print('输入：{}\t结果：{}'.format(numss[i], threeSum(numss[i])))


def threeSumSimpler(nums: [int]):
    length = len(nums)
    nums.sort()
    result = []
    # 枚举a
    for first in range(length):
        # 需要和上一个枚举的不同
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        # c 初始指向数组最右端
        third = length - 1
        target = -nums[first]
        for second in range(first + 1, length):
            # 需要和上一个枚举的不同
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            # 需要保证 b 在 c 的左侧
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            # 如果 b 和 c 重合，之后就不会有满足 a + b + c = 0 的情况了
            if second == third:
                break
            if nums[second] + nums[third] == target:
                result.append([nums[first], nums[second], nums[third]])
    return result


numss = [[-1, 0, 1, 2, -1, -4], [], [0]]
for i in range(len(numss)):
    print('输入：{}\t结果：{}'.format(numss[i], threeSumSimpler(numss[i])))

