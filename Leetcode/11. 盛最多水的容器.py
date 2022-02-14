# 11. 盛最多水的容器
# 给你 n1 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n1 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且n的值至少为 2。
def maxArea(height):
    area = 0
    for i in range(len(height) - 1):
        for j in range(i, len(height)):
            area = max(((j - i) * min([height[j], height[i]])), area)
    return area


heights = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [4, 3, 2, 1, 4], [1, 2, 1]]
for i in range(len(heights)):
    print('输入：', heights[i], '\t结果：', maxArea(heights[i]))


def maxAreaDoublePointer(height):
    result = 0
    left, right = 0, len(height) - 1
    while left < right:
        currentHeight = min(height[left], height[right])
        result = max(currentHeight * (right - left), result)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result


heights = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [4, 3, 2, 1, 4], [1, 2, 1]]
for i in range(len(heights)):
    print('输入：', heights[i], '\t结果：', maxAreaDoublePointer(heights[i]))
