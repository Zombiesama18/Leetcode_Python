# 1011. 在 D 天内送达包裹的能力（需要复习）
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
def shipWithinDaysByTestingOneByOne(weights: [int], D: int) -> int:
    maxWeight = max(weights)
    while True:
        currentNItemSum = 0
        requiredDays = 1
        for weight in weights:
            if currentNItemSum + weight > maxWeight:
                currentNItemSum = weight
                requiredDays += 1
            else:
                currentNItemSum += weight
        if requiredDays <= D:
            break
        else:
            maxWeight += 1
    return maxWeight


weightss = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 2, 2, 4, 1, 4], [1, 2, 3, 1, 1]]
Ds = [5, 3, 4]
shipWithinDaysByTestingOneByOne(weightss[0], Ds[0])


def shipWithinDaysByBinarySearch(weights: [int], D: int) -> int:
    leftSide, rightSide = max(weights), sum(weights)
    while leftSide < rightSide:
        middle = (leftSide + rightSide) // 2
        requiredDays, currentWeight = 1, 0
        for weight in weights:
            if currentWeight + weight > middle:
                currentWeight = weight
                requiredDays += 1
            else:
                currentWeight += weight
        if requiredDays <= D:
            rightSide = middle
        else:
            leftSide = middle + 1
    return leftSide


for i in range(len(weightss)):
    print('Input: weights = {}, D = {}\tOutput: {}'.format(weightss[i], Ds[i],
                                                           shipWithinDaysByBinarySearch(weightss[i], Ds[i])))


