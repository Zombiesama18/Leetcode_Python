"""
630. 课程表 III
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，
其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
返回你最多可以修读的课程数目。
"""
import heapq


def scheduleCourse(courses: [[int]]) -> int:
    courses.sort(key=lambda x: x[1])
    total_time = 0
    q = []
    for t_i, d_i in courses:
        if total_time + t_i <= d_i:
            total_time += t_i
            heapq.heappush(q, -t_i)
        elif q and -q[0] > t_i:
            total_time -= -q[0] - t_i
            heapq.heappop(q)
            heapq.heappush(q, -t_i)
    return len(q)


