#!/usr/bin/env Python
# coding=utf-8
# 1981. 最小化目标值与所选元素的差（需要复习）
# 给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。
# 从矩阵的 每一行 中选择一个整数，你的目标是最小化 所有选中元素之 和 与目标值 target 的 绝对差 。
# 返回 最小的绝对差 。
# a 和 b 两数字的 绝对差 是 a - b 的绝对值。
def minimizeTheDifference(mat: [[int]], target: int) -> int:
    row = len(mat)
    sumOfLastRow = {0}
    for i in range(row):
        sumOfThisRow = set()
        for num in mat[i]:
            for sumNumber in sumOfLastRow:
                sumOfThisRow.add(num + sumNumber)
        sumOfLastRow = sumOfThisRow
    result = float('INF')
    for num in sumOfLastRow:
        result = min(result, abs(target - num))
    return result


minimizeTheDifference([[1,2,3],[4,5,6],[7,8,9]], 13)
minimizeTheDifference([[1],[2],[3]], 100)
minimizeTheDifference([[1,2,9,8,7]], 6)


