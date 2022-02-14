# 面试题 17.21. 直方图的水量（需要复习）
# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。感谢 Marcos 贡献此图。
# url: https://leetcode-cn.com/problems/volume-of-histogram-lcci/
def trap(height: [int]) -> int:
    length = len(height)
    highOfLastEdge = 0
    heightsFromLeft = [0 for _ in range(length)]
    heightsFromRight = [0 for _ in range(length)]
    result = 0
    for i in range(0, length):
        if height[i] > highOfLastEdge:
            highOfLastEdge = height[i]
        else:
            heightsFromLeft[i] = highOfLastEdge - height[i]
    highOfLastEdge = 0
    for i in range(length - 1, -1, -1):
        if height[i] > highOfLastEdge:
            highOfLastEdge = height[i]
        else:
            heightsFromRight[i] = highOfLastEdge - height[i]
    for i in range(length):
        result += min(heightsFromLeft[i], heightsFromRight[i])
    return result


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [5, 4, 1, 2]
height = [4, 2, 0, 3, 2, 5]
trap(height)
