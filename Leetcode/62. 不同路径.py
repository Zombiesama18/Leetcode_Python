# 62. 不同路径
# 一个机器人位于一个 m x n1 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？


def uniquePaths(m, n):
    finish = [n, m]

    def recursion(now, direction):
        global counter
        temp = [now[0] + direction[0], now[1] + direction[1]]
        if temp == finish:
            counter += 1
            return
        if temp[0] < finish[0]:
            recursion(temp, [1, 0])
        if temp[1] < finish[1]:
            recursion(temp, [0, 1])

    recursion([1, 1], [1, 0])
    recursion([1, 1], [0, 1])
    return


counter = 0
m = 7
n = 3
uniquePaths(m, n)
print(counter)
