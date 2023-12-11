"""
1305. 两棵二叉搜索树中的所有元素
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.
"""
from typing import List
from libraries.utils import TreeNode


def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    def traverse(node: TreeNode, numList: List[int]):
        if not node:
            return
        traverse(node.left, numList)
        numList.append(node.val)
        traverse(node.right, numList)
        return

    root1List, root2List = [], []
    traverse(root1, root1List)
    traverse(root2, root2List)
    root1Index, root2Index = 0, 0
    result = []
    while root1Index < len(root1List) or root2Index < len(root2List):
        if root1Index == len(root1List):
            result.append(root2List[root2Index])
            root2Index += 1
        elif root2Index == len(root2List):
            result.append(root1List[root1Index])
            root1Index += 1
        else:
            if root1List[root1Index] == root2List[root2Index]:
                result.append(root1List[root1Index])
                result.append(root1List[root1Index])
                root1Index += 1
                root2Index += 1
            elif root1List[root1Index] < root2List[root2Index]:
                result.append(root1List[root1Index])
                root1Index += 1
            else:
                result.append(root2List[root2Index])
                root2Index += 1
    return result


a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(4)
b = TreeNode(1)
b.left = TreeNode(0)
b.right = TreeNode(3)
getAllElements(a, b)



