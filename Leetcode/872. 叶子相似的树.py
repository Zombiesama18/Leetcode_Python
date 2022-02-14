from libraries.utils import TreeNode, generateTreebyLevelOrder


# 872. 叶子相似的树
# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    leafValue1, leafValue2 = [], []

    def leafSimilarHelper(node: TreeNode, leafValue: []):
        if not node.left and not node.right:
            leafValue.append(node.val)
            return
        if node.left:
            leafSimilarHelper(node.left, leafValue)
        if node.right:
            leafSimilarHelper(node.right, leafValue)

    leafSimilarHelper(root1, leafValue1)
    leafSimilarHelper(root2, leafValue2)
    return leafValue1 == leafValue2


leafSimilar(generateTreebyLevelOrder([3,5,1,6,7,4,2,None,None,None,None,None,None,9,11,None,None,None,None,None,None,None,None,None,None,None,None,None,None,8,10]),
            generateTreebyLevelOrder([3,5,1,6,2,9,8,None,None,7,4]))
