from libraries.utils import TreeNode, generateTreebyLevelOrder


# 938. 二叉搜索树的范围和
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    def rangeSumHelper(node: TreeNode, sum: int, low: int, high: int):
        if not node:
            return sum
        if low <= node.val <= high:
            sum += node.val
            sum = rangeSumHelper(node.left, sum, low, high)
            sum = rangeSumHelper(node.right, sum, low, high)
        elif node.val < low:
            sum = rangeSumHelper(node.right, sum, low, high)
        else:
            sum = rangeSumHelper(node.left, sum, low, high)
        return sum

    result = rangeSumHelper(root, 0, low, high)
    return result


roots = [generateTreebyLevelOrder([10, 5, 15, 3, 7, None, 18]),
         generateTreebyLevelOrder([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None])]
lows = [7, 6]
highs = [15, 10]
output = rangeSumBST(roots[1], lows[1], highs[1])
