# 56. 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。


def merge(intervals):
    output = []
    result = []
    intervals.sort()
    for i in range(0, (len(intervals)) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            output.append([intervals[i][0], intervals[i + 1][1]])
        else:
            output.append(intervals[i])
    output.append(intervals[-1])
    result.append(output[0])
    for i in range(1, len(output)):
        if not (output[i][0] >= output[i - 1][0] and output[i][1] <= output[i - 1][1]):
            result.append(output[i])
    return result


intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
merge(intervals)
