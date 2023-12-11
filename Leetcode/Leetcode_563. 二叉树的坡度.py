"""
563. 二叉树的坡度
给定一个二叉树，计算 整个树 的坡度 。
一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；
没有右子树的话也是一样。空结点的坡度是 0 。
整个树 的坡度就是其所有节点的坡度之和。
"""
from libraries.utils import TreeNode


def findTilt(root: TreeNode) -> int:
    result = 0

    def helper(node):
        if not node:
            return 0
        nonlocal result
        sum_left = helper(node.left)
        sum_right = helper(node.right)
        result += abs(sum_right - sum_left)
        return sum_left + sum_right + node.val

    helper(root)
    return result


