"""
1080. 根到叶路径上的不足节点

给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
叶子节点，就是没有子节点的节点。
"""
from libraries.utils import TreeNode
from typing import Optional


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return root if self.traverse_add(root, 0, limit) else None

    def traverse_add(self, node: TreeNode, sum_so_far: int, limit: int):
        if not node:
            return False
        if not node.left and not node.right:
            return node.val + sum_so_far >= limit
        have_sufficient_left = self.traverse_add(node.left, sum_so_far + node.val, limit)
        have_sufficient_right = self.traverse_add(node.right, sum_so_far + node.val, limit)
        if not have_sufficient_left:
            node.left = None
        if not have_sufficient_right:
            node.right = None
        return have_sufficient_left or have_sufficient_right




