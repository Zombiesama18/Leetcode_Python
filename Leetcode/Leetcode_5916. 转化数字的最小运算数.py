# 5916. 转化数字的最小运算数
# 给你一个下标从 0 开始的整数数组 nums ，该数组由 互不相同 的数字组成。另给你两个整数 start 和 goal 。
# 整数 x 的值最开始设为 start ，你打算执行一些运算使 x 转化为 goal 。你可以对数字 x 重复执行下述运算：
# 如果 0 <= x <= 1000 ，那么，对于数组中的任一下标 i（0 <= i < nums.length），可以将 x 设为下述任一值：
# x + nums[i]
# x - nums[i]
# x ^ nums[i]（按位异或 XOR）
# 注意，你可以按任意顺序使用每个 nums[i] 任意次。使 x 越过 0 <= x <= 1000 范围的运算同样可以生效，但该该运算执行后将不能执行其他运算。
# 返回将 x = start 转化为 goal 的最小操作数；如果无法完成转化，则返回 -1 。
import collections


def minimumOperations(nums: [int], start: int, goal: int) -> int:
    pq = collections.deque([(start, 0)])
    traversedSet = set()
    while pq:
        currentNumber, step = pq.popleft()
        if currentNumber == goal:
            return step
        if currentNumber < 0 or currentNumber > 1000 or currentNumber in traversedSet:
            continue
        traversedSet.add(currentNumber)
        for num in nums:
            pq.append((currentNumber + num, step + 1))
            pq.append((currentNumber - num, step + 1))
            pq.append((currentNumber ^ num, step + 1))
    return -1


minimumOperations([1,3], 6, 4)
minimumOperations([2,4,12], 2, 12)
minimumOperations([3,5,7], 0, -4)
minimumOperations([2,8,16], 0, -1)
minimumOperations([1], 0, 3)
minimumOperations([-21,36,-12,43,-4,-52,-93,5,12,81,-90,7,-31,-97,-49,93,-65,82,-37,29,87,-36,70,51,60,-19,-73,-32,-13,-51,-23,50], 4, 789)
