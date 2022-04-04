"""
589. N 叉树的前序遍历
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: 'Node') -> List[int]:
    result = []

    def search(node):
        if not node:
            return
        result.append(node.val)
        for child in node.children:
            search(child)

    search(root)
    return result
