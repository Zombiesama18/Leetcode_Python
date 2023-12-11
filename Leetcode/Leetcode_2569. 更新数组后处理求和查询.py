"""
2569. 更新数组后处理求和查询

给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成 0 。
l 和 r 下标都从 0 开始。
操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
请你返回一个数组，包含所有第三种操作类型的答案。
"""
import itertools
from typing import List


class SegNode:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.sum = 0
        self.lazytag = False


class SegTree:
    def __init__(self, nums):
        self.arr = [SegNode() for _ in range(len(nums) * 4 + 1)]
        self.build(1, 0, len(nums) - 1, nums)

    def build(self, ids, l, r, nums):
        arr = self.arr
        arr[ids] = SegNode()
        arr[ids].l = l
        arr[ids].r = r
        arr[ids].lazytag = False
        if l == r:
            arr[ids].sum = nums[l]
            return
        mid = (l + r) // 2
        self.build(2 * ids, l, mid, nums)
        self.build(2* ids + 1, mid + 1, r, nums)
        arr[ids].sum = arr[2 * ids].sum + arr[2 * ids + 1].sum

    def pushdown(self, x):
        arr = self.arr
        if arr[x].lazytag:
            arr[2 * x].lazytag = not arr[2 * x].lazytag
            arr[2 * x].sum = arr[2 * x].r - arr[2 * x].l + 1 - arr[2 * x].sum
            arr[2 * x + 1].lazytag = not arr[2 * x + 1].lazytag
            arr[2 * x + 1].sum = arr[2 * x + 1].r - arr[2 * x + 1].l + 1 - arr[2 * x + 1].sum
            arr[x].lazytag = False

    def modify(self, ids, l, r):
        arr = self.arr
        if arr[ids].l >= l and arr[ids].r <= r:
            arr[ids].sum = (arr[ids].r - arr[ids].l + 1) - arr[ids].sum
            arr[ids].lazytag = not arr[ids].lazytag
            return
        self.pushdown(ids)
        mid = (arr[ids].l + arr[ids].r) // 2
        if arr[2 * ids].r >= l:
            self.modify(2 * ids, l, r)
        if arr[2 * ids + 1].l <= r:
            self.modify(2 * ids + 1, l, r)
        arr[ids].sum = arr[2 * ids].sum + arr[2 * ids + 1].sum

    def query(self, ids, l, r):
        arr = self.arr
        if arr[ids].l >= l and arr[ids].r <= r:
            return arr[ids].sum
        if arr[ids].r < l or arr[ids].l > r:
            return 0
        self.pushdown(ids)
        mid = (arr[ids].l + arr[ids].r) // 2
        result = 0
        if arr[2 * ids].r >= 1:
            result += self.query(2 * ids, l, r)
        if arr[2 * ids + 1].l <= r:
            result += self.query(2 *ids + 1, l, r)
        return result

    def sum_range(self, left, right):
        return self.query(1, left, right)

    def reverse_range(self, left, right):
        self.modify(1, left, right)


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        seg_tree = SegTree(nums1)
        total = sum(nums2)
        result = []
        for query in queries:
            if query[0] == 1:
                l = query[1]
                r = query[2]
                seg_tree.reverse_range(l, r)
            elif query[0] == 2:
                total += seg_tree.sum_range(0, len(nums1) - 1) * query[1]
            elif query[0] == 3:
                result.append(total)
        return result

