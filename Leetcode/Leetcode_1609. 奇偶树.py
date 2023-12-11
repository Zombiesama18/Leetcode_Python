"""
1609. 奇偶树
如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：
二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。
"""
import collections

from libraries.utils import TreeNode
from typing import Optional


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, layerNum):
            if layerNum % 2 == 0 and node.val % 2 == 0:
                return False
            if layerNum % 2 == 1 and node.val % 2 == 1:
                return False
            return True

        lastLayer = -1
        q = collections.deque([(root, 0)])
        while q:
            currentNode, layer = q.popleft()
            if layer != lastLayer:
                if not isValid(currentNode, layer):
                    return False
                layerNumber = [currentNode.val]
                lastLayer = layer
            else:
                if layer % 2 == 0 and (not isValid(currentNode, layer) or currentNode.val <= layerNumber[-1]):
                    return False
                if layer % 2 == 1 and (not isValid(currentNode, layer) or currentNode.val >= layerNumber[-1]):
                    return False
                layerNumber.append(currentNode.val)
            if currentNode.left:
                q.append((currentNode.left, layer + 1))
            if currentNode.right:
                q.append((currentNode.right, layer + 1))
        return True



