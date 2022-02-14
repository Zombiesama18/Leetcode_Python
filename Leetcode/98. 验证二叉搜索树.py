class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 98. 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
def isValidBST(root):
    if root.left:
        if root.left.val > root.val:
            return False
        else:
            isValidBST(root.left)
    if root.right:
        if root.right.val < root.val:
            return False
        else:
            isValidBST(root.right)
    return True


l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(6)
l5.left = l1
l5.right = l4
l4.left = l3
l4.right = l6
isValidBST(l5)
l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l2.left = l1
l2.right = l3
isValidBST(l2)
