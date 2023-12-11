# 1979. 找出数组的最大公约数
# 给你一个整数数组 nums ，返回数组中最大数和最小数的 最大公约数 。
# 两个数的 最大公约数 是能够被两个数整除的最大正整数。
import math


def findGCD(nums: [int]) -> int:
    biggerNumber = max(nums)
    smallerNumber = min(nums)
    while biggerNumber % smallerNumber != 0:
        tempNumber = smallerNumber
        smallerNumber = biggerNumber % smallerNumber
        biggerNumber = tempNumber
    return smallerNumber


findGCD([2,5,6,9,10])
findGCD([7,5,6,8,3])
findGCD([3,3])


def findGCD(nums: [int]) -> int:
    biggerNumber = max(nums)
    smallerNumber = min(nums)
    return math.gcd(biggerNumber, smallerNumber)

