"""
5986. 设置时间的最少代价
常见的微波炉可以设置加热时间，且加热时间满足以下条件：
至少为 1   秒钟。
至多为   99   分   99   秒。
你可以 最多   输入   4 个数字   来设置加热时间。如果你输入的位数不足 4 位，微波炉会自动加 前缀   0   来补足 4 位。
微波炉会将设置好的四位数中，前   两位当作分钟数，后   两位当作秒数。它们所表示的总时间就是加热时间。比方说：
你输入   9 5 4   （三个数字），被自动补足为   0954   ，并表示   9   分   54   秒。
你输入   0 0 0 8   （四个数字），表示   0   分   8   秒。
你输入   8 0 9 0   ，表示   80   分   90   秒。
你输入   8 1 3 0   ，表示   81   分   30   秒。
给你整数   startAt   ，moveCost   ，pushCost   和   targetSeconds   。一开始，你的手指在数字   startAt   处。将
手指移到   任何其他数字   ，需要花费   moveCost   的单位代价。每   输入你手指所在位置的数字一次，需要花费   pushCost   的单位代价。
要设置   targetSeconds   秒的加热时间，可能会有多种设置方法。你想要知道这些方法中，总代价最小为多少。
请你能返回设置   targetSeconds   秒钟加热时间需要花费的最少代价。
请记住，虽然微波炉的秒数最多可以设置到 99   秒，但一分钟等于   60   秒。
"""


def minCostSetTime(startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
    possibleInput = []
    if targetSeconds < 60:
        possibleInput.append(str(targetSeconds))
    elif targetSeconds < 100:
        possibleInput.append(str(targetSeconds))
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60
        possibleInput.append(str(minutes) + '0' * (2 - len(str(seconds))) + str(seconds))
    else:
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60
        if seconds + 60 < 100:
            possibleInput.append(str(minutes - 1) + str(seconds + 60))
        if minutes < 100:
            possibleInput.append(str(minutes) + '0' * (2 - len(str(seconds))) + str(seconds))
    result = float('INF')
    for inputs in possibleInput:
        currentNumber = str(startAt)
        timeCost = 0
        for char in inputs:
            if char != currentNumber:
                timeCost += moveCost
            timeCost += pushCost
            currentNumber = char
        result = min(result, timeCost)
    return result


minCostSetTime(1, 9403, 9402, 6008)
