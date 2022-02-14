# 42. 接雨水
# 给定 n1 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


def trap(heights):
    area = []
    if sum(heights) == 0 or sum(heights) == 1:
        return 0
    for i in range(len(heights)):
        if heights[i] != 0:
            heights = heights[i:]
            break
    for i in range(len(heights) - 1, 0, -1):
        if heights[i] != 0:
            heights = heights[:i + 1]
            break

    def edgearea(edge, direction):
        if direction == 'left':
            sub_heights = heights[:edge]
            left_upper = edge - 1
            while sub_heights:
                sub_index = []
                for i in range(0, len(sub_heights)):
                    if sub_heights[i] == max(sub_heights):
                        sub_index.append(i)
                get_area([sub_index[0], left_upper], 'left')
                sub_heights = heights[:sub_index[0]]
                left_upper = sub_index[0] - 1
        if direction == 'right':
            sub_heights = heights[edge + 1:]
            right_lower = edge + 1
            while sub_heights:
                sub_index = []
                for i in range(0, len(sub_heights)):
                    if sub_heights[i] == max(sub_heights):
                        sub_index.append(i + right_lower)
                get_area([right_lower, sub_index[-1]], 'right')
                sub_heights = heights[sub_index[-1] + 1:]
                right_lower = sub_index[-1] + 1

    def get_area(index, pattern):
        if pattern == 'left':
            for i in range(index[0], index[1] + 1):
                area.append(heights[index[0]] - heights[i])
        if pattern == 'right':
            for i in range(index[0], index[1] + 1):
                area.append(heights[index[1]] - heights[i])
        if pattern == 'equal':
            for i in range(index[0], index[1]):
                area.append(heights[index[0]] - heights[i])

    if heights.count(max(heights)) == 1:
        center = heights.index(max(heights))
        edgearea(center, 'left')
        edgearea(center, 'right')
    else:
        index_list = []
        for i in range(0, len(heights)):
            if heights[i] == max(heights):
                index_list.append(i)
        center1 = index_list[0]
        center2 = index_list[-1]
        get_area([center1, center2], 'equal')
        edgearea(center1, 'left')
        edgearea(center2, 'right')
    return sum(area)


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trap(heights)
