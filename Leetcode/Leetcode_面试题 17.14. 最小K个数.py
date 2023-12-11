# 面试题 17.14. 最小K个数
# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
import heapq


def smallestK(arr: [int], k: int) -> [int]:
    length = len(arr)
    result = []
    for i in range(k):
        result.append(- arr[i])
    heapq.heapify(result)
    minusOfMaxNumber = result[0]
    for i in range(k, length):
        if - arr[i] > minusOfMaxNumber:
            heapq.heappush(result, - arr[i])
            heapq.heappop(result)
            minusOfMaxNumber = result[0]
    output = []
    for item in result:
        output.append(-item)
    return output


smallestK([1,3,5,7,2,4,6,8], 4)


def smallestKAnother(arr: [int], k: int) -> [int]:
    length = len(arr)
    result = []
    for i in range(k):
        result.append(- arr[i])
    heapq.heapify(result)
    for i in range(k, length):
        heapq.heappushpop(result, - arr[i])
    output = []
    for item in result:
        output.append(-item)
    return output


smallestKAnother([1,3,5,7,2,4,6,8], 4)
