from libraries.utils import TreeNode


# 671. 二叉树中第二小的节点
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
def findSecondMinimumValue(root: TreeNode) -> int:
    result, rootValue = -1, root.val

    def DFS(node: TreeNode):
        nonlocal result
        if not node or (result != -1 and node.val >= result):
            return
        if node.val > rootValue:
            result = node.val
        DFS(node.left)
        DFS(node.right)

    DFS(root)
    return result



