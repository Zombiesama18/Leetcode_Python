from libraries.utils import TreeNode


# 863. 二叉树中所有距离为 K 的结点
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
def distanceK(root: TreeNode, target: TreeNode, k: int) -> [int]:
    treeNodeDict, result = {}, []

    def findParents(node: TreeNode):
        if node.left:
            treeNodeDict[node.left.val] = node
            findParents(node.left)
        if node.right:
            treeNodeDict[node.right.val] = node
            findParents(node.right)

    def findNode(node: TreeNode, fromNode: TreeNode, depth: int, k: int):
        if not node:
            return
        if depth == k:
            result.append(node.val)
            return
        if node.left != fromNode:
            findNode(node.left, node, depth + 1, k)
        if node.right != fromNode:
            findNode(node.right, node, depth + 1, k)
        if node.val in treeNodeDict and treeNodeDict[node.val] != fromNode:
            findNode(treeNodeDict[node.val], node, depth + 1, k)

    findParents(root)
    findNode(target, None, 0, k)
    return result




