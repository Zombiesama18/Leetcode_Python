"""
剑指 Offer II 040. 矩阵中最大的矩形
给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。
注意：此题 matrix 输入格式为一维 01 字符串数组。
"""
from typing import List


def maximalRectangle(matrix: List[str]) -> int:
    def helper(heights):
        stack = [(-1, -1)]
        heights += [0]
        answer = 0
        for i, h in enumerate(heights):
            while stack[-1][1] > h:
                _, oh = stack.pop()
                s = (i - stack[-1][0] - 1) * oh
                answer = max(answer, s)
            stack.append((i, h))
        return answer

    if not matrix:
        return 0
    row, col = len(matrix), len(matrix[0])
    dp = [0] * col
    result = 0
    for i in range(row):
        for j in range(col):
            dp[j] = 0 if matrix[i][j] == '0' else dp[j] + 1
        result = max(result, helper(dp))
    return result


maximalRectangle(matrix = ["10100","10111","11111","10010"])
