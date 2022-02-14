def binarySearch(series, target):
    low = -1
    high = len(series) - 1
    while low < high:
        mid = (low + high + 1) // 2
        if target < series[mid]:
            high = mid - 1
        else:
            low = mid
    return low
