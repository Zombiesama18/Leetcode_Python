# 84. 柱状图中最大的矩形
# 给定 n1 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


def largestRectangleArea(heights):
    areas = heights[:]
    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            areas.append(min(heights[i: j + 1]) * (j - i + 1))
    return max(areas)


heights = [2, 1, 5, 6, 2, 3]
largestRectangleArea(heights)
