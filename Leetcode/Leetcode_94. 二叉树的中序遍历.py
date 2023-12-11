# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历（左，根，右）。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    values = []

    def recursion(node):
        if node.left:
            recursion(node.left)
        values.append(node.val)
        if node.right:
            recursion(node.right)

    recursion(root)
    return values


l3 = TreeNode(3)
l2 = TreeNode(2)
l1 = TreeNode(1)
l1.right = l2
l2.left = l3
inorderTraversal(l1)
