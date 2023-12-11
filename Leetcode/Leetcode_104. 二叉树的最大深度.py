class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
def maxDepth(root):
    depths = []

    def recursion(node, depth):
        if not node.left and not node.right:
            depths.append(depth)
            return
        if node.left:
            recursion(node.left, depth + 1)
        if node.right:
            recursion(node.right, depth + 1)
        return

    recursion(root, 1)
    return max(depths)


l1 = TreeNode(3)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)
l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5
maxDepth(l1)
