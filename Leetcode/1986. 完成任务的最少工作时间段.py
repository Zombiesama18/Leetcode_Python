# 1986. 完成任务的最少工作时间段
# 你被安排了 n 个任务。任务需要花费的时间用长度为 n 的整数数组 tasks 表示，第 i 个任务需要花费 tasks[i] 小时完成。一个 工作时间段 中，你可以 至多 连续工作 sessionTime 个小时，然后休息一会儿。
# 你需要按照如下条件完成给定任务：
# 如果你在某一个时间段开始一个任务，你需要在 同一个 时间段完成它。
# 完成一个任务后，你可以 立马 开始一个新的任务。
# 你可以按 任意顺序 完成任务。
# 给你 tasks 和 sessionTime ，请你按照上述要求，返回完成所有任务所需要的 最少 数目的 工作时间段 。
# 测试数据保证 sessionTime 大于等于 tasks[i] 中的 最大值 。
def minSessions(tasks: [int], sessionTime: int) -> int:
    length = len(tasks)
    valid = [False for _ in range(1 << length)]
    for mask in range(1, 1 << length):
        needTime = 0
        for i in range(length):
            if (1 << i) & mask:
                needTime += tasks[i]
        if needTime <= sessionTime:
            valid[mask] = True

    field = [float('INF')] * (1 << length)
    field[0] = 0
    for mask in range(1, 1 << length):
        subset = mask
        while subset:
            if valid[subset]:
                field[mask] = min(field[mask], field[mask ^ subset] + 1)
            subset = (subset - 1) & mask
    return field[-1]


