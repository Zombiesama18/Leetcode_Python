"""
1026. 节点与其祖先之间的最大差值

给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）
"""
from typing import Optional
from libraries.utils import TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.traverse_helper(0, float('inf'), root)
        return self.result

    def traverse_helper(self, anc_max: int, anc_min: int, current_node: TreeNode):
        if not current_node:
            return
        if current_node.val < anc_min:
            anc_min = current_node.val
        if current_node.val > anc_max:
            anc_max = current_node.val
        self.result = max(self.result, anc_max - anc_min)
        self.traverse_helper(anc_max, anc_min, current_node.left)
        self.traverse_helper(anc_max, anc_min, current_node.right)
