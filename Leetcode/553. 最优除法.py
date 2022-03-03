"""
553. 最优除法
给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。
但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，
才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。
"""
from typing import *


def optimalDivisionDP(nums: List[int]) -> str:
    class Node:
        def __init__(self, minVal=10000, maxVal=0):
            self.minVal = minVal
            self.maxVal = maxVal
            self.minStr = ''
            self.maxStr = ''

    length = len(nums)
    dp = [[Node() for _ in range(length)] for _ in range(length)]
    for i in range(length):
        dp[i][i].minVal = nums[i]
        dp[i][i].maxVal = nums[i]
        dp[i][i].minStr = str(nums[i])
        dp[i][i].maxStr = str(nums[i])
    for i in range(length):
        for j in range(length - i):
            for k in range(j, j + i):
                if dp[j][j + i].maxVal < dp[j][k].maxVal / dp[k + 1][j + 1].minVal:
                    dp[j][j + i].maxVal = dp[j][k].maxVal / dp[k + 1][j + 1].minVal
                    if k + 1 == j + i:
                        dp[j][j + i].maxStr = dp[j][k].maxStr + '/' + dp[k + 1][j + i].minStr
                    else:
                        dp[j][j + i].maxStr = dp[j][k].maxStr + '/(' + dp[k + 1][j + i].minStr + ')'
                if dp[j][j + i].minVal > dp[j][k].minVal / dp[k + 1][j + i].maxVal:
                    dp[j][j + i].minVal = dp[j][k].minVal / dp[k + 1][j + i].maxVal
                    if k + 1 == j + i:
                        dp[j][j + i].minStr = dp[j][k].minStr + '/' + dp[k + 1][j + i].maxStr
                    else:
                        dp[j][j + i].minStr = dp[j][k].minStr + '/(' + dp[k + 1][j + i].maxStr + ')'
    return dp[0][length - 1].maxStr


def optimalDivision(nums: List[int]) -> str:
    if len(nums) == 1:
        return str(nums[0])
    if len(nums) == 2:
        return f'{nums[0]}/{nums[1]}'
    return f'{nums[0]}/(' + '/'.join(map(str, nums[1:])) + ')'


