"""
307. 区域和检索 - 数组可修改
给你一个数组 nums ，请你完成两类查询。
其中一类查询要求 更新 数组 nums 下标对应的值
另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：
NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值 更新 为 val
int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和
（即，nums[left] + nums[left + 1], ..., nums[right]）
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.blockSize = int(len(nums) ** 0.5)
        self.blockSums = [0] * ((len(nums) + self.blockSize - 1) // self.blockSize)
        for i in range(len(nums)):
            self.blockSums[i // self.blockSize] += nums[i]

    def update(self, index: int, val: int) -> None:
        self.blockSums[index // self.blockSize] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        blockIndex1, blockIndex2 = left // self.blockSize, right // self.blockSize
        if blockIndex1 == blockIndex2:
            return sum(self.nums[left: right + 1])
        return sum(self.nums[left: (blockIndex1 + 1) * self.blockSize] +
                   self.blockSums[blockIndex1 + 1: blockIndex2] +
                   self.nums[blockIndex2 * self.blockSize: right + 1])
