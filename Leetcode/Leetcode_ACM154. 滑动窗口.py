def slidingWindow(nums: [], k: int):
    leftSide, rightSide = 0, -1
    length = len(nums)
    result = []
    state = [0 for _ in range(1000)]
    for i in range(length):
        if i - k + 1 > state[leftSide]:
            leftSide += 1
        while leftSide <= rightSide and nums[i] <= nums[state[rightSide]]:
            rightSide -= 1
        rightSide += 1
        state[rightSide] = i
        if i + 1 >= k:
            result.append(nums[state[leftSide]])
    return result


slidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)

