# 1310. 子数组异或查询
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。
# 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。
# 并返回一个包含给定查询 queries 所有结果的数组。
def xorQueriesByCreatingDictionary(arr: [int], queries: [[int]]) -> [int]:
    dictionaryLength = len(arr)
    dictionary = [[0] * dictionaryLength for _ in range(dictionaryLength)]
    for i in range(dictionaryLength):
        for j in range(i, dictionaryLength):
            if i == j:
                dictionary[i][j] = arr[i]
            else:
                dictionary[i][j] = dictionary[i][j - 1] ^ arr[j]
    resultLength = len(queries)
    result = [0] * resultLength
    for i in range(resultLength):
        result[i] = dictionary[queries[i][0]][queries[i][1]]
    return result


xorQueriesByCreatingDictionary([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])


def xorQueries(arr: [int], queries: [[int]]) -> [int]:
    length = len(arr)
    presum = [0 for _ in range(length + 1)]
    for i in range(length):
        presum[i + 1] = presum[i] ^ arr[i]
    result = []
    for leftSide, rightSide in queries:
        result.append(presum[leftSide] ^ presum[rightSide + 1])
    return result

