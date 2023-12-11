class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 102. 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


def levelOrder(root):
    values = []

    def recursion(node, layer):
        if len(values) < layer + 1:
            values.append([])
        values[layer].append(node.val)
        if not node.left and not node.right:
            return
        if node.left:
            recursion(node.left, layer + 1)
        if node.right:
            recursion(node.right, layer + 1)
        return

    recursion(root, 0)
    return values


l1 = TreeNode(3)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)
l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5
levelOrder(l1)
