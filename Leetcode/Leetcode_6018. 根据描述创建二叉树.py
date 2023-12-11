"""
6018. 根据描述创建二叉树
给你一个二维整数数组 descriptions ，其中 descriptions[i] = [parenti, childi, isLefti]
表示 parenti 是 childi 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。此外：
如果 isLefti == 1 ，那么 childi 就是 parenti 的左子节点。
如果 isLefti == 0 ，那么 childi 就是 parenti 的右子节点。
请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。
测试用例会保证可以构造出 有效 的二叉树。
"""
import collections
from typing import List, Optional
from libraries.utils import TreeNode


def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    valueDictionary = dict()
    parents, children = set(), set()
    for source, destination, isLeft in descriptions:
        parents.add(source)
        children.add(destination)
        if source not in valueDictionary:
            valueDictionary[source] = TreeNode(source)
        if destination not in valueDictionary:
            valueDictionary[destination] = TreeNode(destination)
        if isLeft == 1:
            valueDictionary[source].left = valueDictionary[destination]
        else:
            valueDictionary[source].right = valueDictionary[destination]
    for parent in parents:
        if parent not in children:
            return valueDictionary[parent]

