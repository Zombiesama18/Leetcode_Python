class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 105. 从前序与中序遍历序列构造二叉树（需要复习）
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。
def buildTree(preorder, inorder):
    if not preorder and not inorder:
        return
    root = TreeNode(preorder[0])
    ind = inorder.index(root.val)
    root.left = buildTree(preorder[1: ind + 1], inorder[:ind])
    root.right = buildTree(preorder[ind + 1:], inorder[ind + 1:])
    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
buildTree(preorder, inorder)