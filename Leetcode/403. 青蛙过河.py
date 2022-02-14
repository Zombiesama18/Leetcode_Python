# 403. 青蛙过河
# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
# 给你石子的位置列表 stones（用单元格序号 升序 表示），请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
# 开始时，青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。另请注意，青蛙只能向前方（终点的方向）跳跃。
def canCrossByEnumerating(stones: [int]) -> bool:
    def canCrossHelper(index: int, stride: int, result: bool):
        if index == len(stones) - 1:
            return True
        nextStep = index + 1
        while stones[nextStep] - stones[index] < stride + 2:
            if stones[nextStep] - stones[index] > stride - 2:
                result = result or canCrossHelper(nextStep, stones[nextStep] - stones[index], result)
            if result or nextStep == len(stones) - 1:
                break
            else:
                nextStep += 1
        return result

    if stones[1] - stones[0] != 1:
        return False
    else:
        output = canCrossHelper(1, 1, False)
    return output


stones = [0,1,3,5,6,8,12,17]
canCrossByEnumerating(stones)
stones = [0,1,2,3,4,8,9,11]
canCrossByEnumerating(stones)
stones = [0,1,3,6,10,15,16,21]
canCrossByEnumerating(stones)
stones = [0,1,3,6,7]
canCrossByEnumerating(stones)


def canCrossByDynamicProgramming(stones: [int]) -> bool:
    length = len(stones)
    dp = [[False] * length for _ in range(length)]
    dp[0][0] = True
    for i in range(1, length):
        if stones[i] - stones[i - 1] > i:
            return False
    for i in range(1, length):
        for j in range(i - 1, -1, -1):
            stride = stones[i] - stones[j]
            if stride > j + 1:
                break
            dp[i][stride] = dp[j][stride - 1] or dp[j][stride] or dp[j][stride + 1]
            if i == length - 1 and dp[i][stride]:
                return True
    return False


stones = [0,1,3,5,6,8,12,17]
canCrossByDynamicProgramming(stones)
stones = [0,1,2,3,4,8,9,11]
canCrossByDynamicProgramming(stones)
stones = [0,1,3,6,10,15,16,21]
canCrossByDynamicProgramming(stones)
stones = [0,1,3,6,7]
canCrossByDynamicProgramming(stones)

