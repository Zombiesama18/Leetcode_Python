"""
965. 单值二叉树
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
"""
from libraries.utils import TreeNode


def isUnivalTree(root: TreeNode) -> bool:
    value = root.val

    def traverse(node):
        if not node:
            return True
        if node.val != value:
            return False
        return traverse(node.left) and traverse(node.right)

    return traverse(root)


