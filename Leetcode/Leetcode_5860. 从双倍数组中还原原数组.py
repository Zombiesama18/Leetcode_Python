# 5860. 从双倍数组中还原原数组
# 一个整数数组 original 可以转变成一个 双倍 数组 changed ，转变方式为将 original 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。
# 给你一个数组 changed ，如果 change 是 双倍 数组，那么请你返回 original数组，否则请返回空数组。original 的元素可以以 任意 顺序返回。
def findOriginalArray(changed: [int]) -> [int]:
    result = []
    if len(changed) % 2 != 0:
        return result
    changedDict = {}
    for num in changed:
        changedDict[num] = changedDict.setdefault(num, 0) + 1
    if 0 in changedDict:
        if changedDict[0] % 2 != 0:
            return []
        for _ in range(changedDict[0] // 2):
            result.append(0)
        changedDict.pop(0)
    changedKeys = list(changedDict.keys())
    changedKeys.sort()
    for key in changedKeys:
        if changedDict[key] == 0:
            continue
        elif changedDict[key] < 0:
            return []
        else:
            if 2 * key in changedDict:
                for _ in range(changedDict[key]):
                    result.append(key)
                changedDict[2 * key] -= changedDict[key]
            else:
                return []
    return result


findOriginalArray([1,3,4,2,6,8])
findOriginalArray([6,3,0,1])
findOriginalArray([0,0,0,0])



