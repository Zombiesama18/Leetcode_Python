"""
391. 完美矩形
给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
"""
import collections


def isRectangleCover(rectangles: [[int]]) -> bool:
    counter, min_x, min_y, max_x, max_y, area = collections.defaultdict(int), rectangles[0][0], rectangles[0][1], \
                                                rectangles[0][2], rectangles[0][3], 0
    for rect in rectangles:
        area += (rect[3] - rect[1]) * (rect[2] - rect[0])
        counter[(rect[0], rect[1])] += 1
        counter[(rect[0], rect[3])] += 1
        counter[(rect[2], rect[1])] += 1
        counter[(rect[2], rect[3])] += 1
        min_x, min_y, max_x, max_y = min(min_x, rect[0]), min(min_y, rect[1]), max(max_x, rect[2]), max(max_y, rect[3])
    if area != (max_y - min_y) * (max_x - min_x) or counter[(min_x, min_y)] != 1 or counter[(min_x, max_y)] != 1 or counter[(max_x, min_y)] != 1 or counter[(max_x, max_y)] != 1:
        return False
    del counter[(min_x, min_y)], counter[(min_x, max_y)], counter[(max_x, min_y)], counter[(max_x, max_y)]
    return all(value == 2 or value == 4 for value in counter.values())





