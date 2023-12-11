from libraries.utils import TreeNode, generateTreebyLevelOrder, inorderTravesal


# 897. 递增顺序搜索树
# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
def increasingBST(root: TreeNode) -> TreeNode:
    result = []

    def subInorderTraversal(node):
        if not node:
            return
        subInorderTraversal(node.left)
        result.append(node.val)
        subInorderTraversal(node.right)
        return

    subInorderTraversal(root)
    sentinel = TreeNode(0)
    currentNode = sentinel
    for num in result:
        currentNode.right = TreeNode(num)
        currentNode = currentNode.right
    return sentinel.right


levelOrders = [[5, 3, 6, 2, 4, None, 8, 1, None, None, None, None, None, 7, 9], [5, 1, 7]]
treeNodes = [generateTreebyLevelOrder([5, 3, 6, 2, 4, None, 8, 1, None, None, None, None, None, 7, 9]),
             generateTreebyLevelOrder([5, 1, 7])]
node = increasingBST(treeNodes[0])
