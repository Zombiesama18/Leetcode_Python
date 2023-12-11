"""
700. 二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
"""
from libraries.utils import TreeNode


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)



