# 575. 分糖果
# 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。
# 返回妹妹可以获得的最大糖果的种类数。
def distributeCandies(candyType: [int]) -> int:
    target = len(candyType) // 2
    candyType = set(candyType)
    return min(target, len(candyType))


distributeCandies([1,1,2,2,3,3])
distributeCandies([1,1,2,3])

