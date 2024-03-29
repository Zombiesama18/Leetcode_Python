"""
429. N 叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: 'Node') -> List[List[int]]:
    result = []

    def traverse(layer: int, node: 'Node'):
        if not node:
            return
        if len(result) < layer:
            result.append([node.val])
        else:
            result[layer - 1].append(node.val)
        for child in node.children:
            traverse(layer + 1, child)

    traverse(1, root)
    return result

