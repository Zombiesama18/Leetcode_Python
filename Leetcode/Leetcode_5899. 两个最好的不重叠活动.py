# 5899. 两个最好的不重叠活动
# 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第 i 个活动开始于 startTimei ，
# 结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。
# 请你返回价值之和的 最大值 。
# 注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。
# 更具体的，如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。
import bisect
import collections
import heapq


def maxTwoEvents(events: [[int]]) -> int:
    eventDict = collections.defaultdict(list)
    for event in events:
        eventDict[event[0]].append([event[1], event[2]])
    startDays = sorted(eventDict.keys())
    length = len(startDays)
    reversedList = [0 for _ in range(length)]
    for i in range(length - 1, -1, -1):
        for event in eventDict[startDays[i]]:
            reversedList[i] = max(event[1], reversedList[i])
        if i != length - 1:
            reversedList[i] = max(reversedList[i], reversedList[i + 1])
    result = 0

    def DFS(currentDay, totalValue):
        nonlocal result
        dayIndex = bisect.bisect_right(startDays, currentDay)
        while dayIndex < length:
            result = max(result, totalValue + reversedList[dayIndex])
            dayIndex += 1
        result = max(totalValue, result)

    for day in startDays:
        for event in eventDict[day]:
            DFS(event[0], event[1])
    return result


maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]])
maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]])
maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]])
maxTwoEvents([[35,90,47],[72,80,70]])
maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]])


def maxTwoEventsFaster(events: [[int]]) -> int:
    length, tempValue, result, hq = len(events), 0, 0, []
    events.sort()
    for i in range(length):
        while hq and hq[0][0] < events[i][0]:
            tempValue = max(tempValue, heapq.heappop(hq)[1])
        result = max(result, tempValue + events[i][2])
        heapq.heappush(hq, (events[i][1], events[i][2]))
    return result
