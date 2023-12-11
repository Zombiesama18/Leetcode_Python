# 230. 二叉搜索树中第K小的元素
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
from libraries.utils import TreeNode


def kthSmallest(root: [TreeNode], k: int) -> int:
    def DFS(node: TreeNode):
        if not node:
            return
        DFS(node.left)
        nums.append(node.val)
        DFS(node.right)
        return

    nums = []
    DFS(root)
    return nums[k - 1]


