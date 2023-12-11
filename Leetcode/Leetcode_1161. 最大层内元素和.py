"""
1161. 最大层内元素和
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
"""
from typing import Optional

from libraries.utils import TreeNode


def maxLevelSum(root: Optional[TreeNode]) -> int:
    currentLayer = [root]
    nextLayer = []
    result = -1
    maxValue = float('-INF')
    layerIndex = 1
    while currentLayer:
        tempValue = 0
        for node in currentLayer:
            tempValue += node.val
            if node.left:
                nextLayer.append(node.left)
            if node.right:
                nextLayer.append(node.right)
        if tempValue > maxValue:
            maxValue = tempValue
            result = layerIndex
        currentLayer = nextLayer
        nextLayer = []
        layerIndex += 1
    return result

