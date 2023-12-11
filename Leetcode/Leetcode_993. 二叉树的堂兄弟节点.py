from libraries.utils import TreeNode


# 993. 二叉树的堂兄弟节点
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
def isCousins(root: TreeNode, x: int, y: int) -> bool:
    nodeDict = {}

    def traverseNode(node: TreeNode, parent, depth: int):
        if not node:
            return
        nodeDict[node.val] = [parent, depth]
        traverseNode(node.left, node.val, depth + 1)
        traverseNode(node.right, node.val, depth + 1)
        return

    traverseNode(root, 0, 0)
    return nodeDict[x][0] != nodeDict[y][0] and nodeDict[x][1] == nodeDict[y][1]


