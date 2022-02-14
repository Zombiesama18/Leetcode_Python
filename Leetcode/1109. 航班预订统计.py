# 1109. 航班预订统计
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi]
# 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
# 请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。
import collections


def corpFlightBookingsSlower(bookings: [[int]], n: int) -> [int]:
    flightDict = {}
    for booking in bookings:
        for i in range(booking[0], booking[1] + 1):
            flightDict[i] = flightDict.setdefault(i, 0) + booking[2]
    result = []
    for i in range(1, n + 1):
        if i in flightDict:
            result.append(flightDict[i])
        else:
            result.append(0)
    return result


corpFlightBookingsSlower([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
corpFlightBookingsSlower([[1, 2, 10], [2, 2, 15]], 2)


def corpFlightBookingsFaster(bookings: [[int]], n: int) -> [int]:
    result = [0] * n
    for left, right, inc in bookings:
        result[left - 1] += inc
        if right < n:
            result[right] -= inc
    for i in range(1, n):
        result[i] += result[i - 1]
    return result


corpFlightBookingsFaster([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
