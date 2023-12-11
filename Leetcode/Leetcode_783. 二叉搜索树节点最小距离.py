from libraries.utils import TreeNode, generateTreebyLevelOrder


# 783. 二叉搜索树节点最小距离
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 结果：竖直方法不如展开方法
def minDiffInBSTByFlatting(root: TreeNode) -> int:
    traversal = []

    def subInorderTraversal(node):
        if not node:
            return
        subInorderTraversal(node.left)
        traversal.append(node.val)
        subInorderTraversal(node.right)
        return

    subInorderTraversal(root)
    minDistance = float('INF')
    for i in range(len(traversal) - 1):
        if abs(traversal[i + 1] - traversal[i]) < minDistance:
            minDistance = abs(traversal[i + 1] - traversal[i])
    return minDistance


levelOrder = [[5, 1, 7], [4, 2, 6, 1, 3], [1, 0, 48, None, None, 12, 49]]
roots = list(map(generateTreebyLevelOrder, levelOrder))
for i in range(len(roots)):
    print('输入：{}\t结果：{}'.format(levelOrder[i], minDiffInBSTByFlatting(roots[i])))


def minDiffInBSTByVertical(root: TreeNode) -> int:
    minDistance = float('INF')

    def minDiffHelper(node: TreeNode, minDistance):
        if node.left:
            minDistance = min(abs(node.left.val - node.val), minDistance)
            tempNode = node.left
            while tempNode.right:
                minDistance = min(abs(tempNode.right.val - node.val), minDistance)
                tempNode = tempNode.right
            minDistance = minDiffHelper(node.left, minDistance)
        if node.right:
            minDistance = min(abs(node.right.val - node.val), minDistance)
            tempNode = node.right
            while tempNode.left:
                minDistance = min(abs(tempNode.left.val - node.val), minDistance)
                tempNode = tempNode.left
            minDistance = minDiffHelper(node.right, minDistance)
        return minDistance

    minDistance = minDiffHelper(root, minDistance)
    return int(minDistance)


levelOrder = [[90, 69, None, 49, 89, None, None, None, 52], [5, 1, 7], [4, 2, 6, 1, 3], [1, 0, 48, None, None, 12, 49]]
roots = list(map(generateTreebyLevelOrder, levelOrder))
for i in range(len(roots)):
    print('输入：{}\t结果：{}'.format(levelOrder[i], minDiffInBSTByVertical(roots[i])))


def minDiffInBSTByDFS(root: TreeNode) -> int:
    last, minDiff = float('INF'), float('INF')

    def DFS(node: TreeNode, last, minDiff):
        if not node:
            return last, minDiff
        last, minDiff = DFS(node.left, last, minDiff)
        if last != float('INF'):
            minDiff = min(minDiff, node.val - last)
        last = node.val
        last, minDiff = DFS(node.right, last, minDiff)
        return last, minDiff

    _, minDiff = DFS(root, last, minDiff)
    return minDiff


levelOrder = [[90, 69, None, 49, 89, None, None, None, 52], [5, 1, 7], [4, 2, 6, 1, 3], [1, 0, 48, None, None, 12, 49]]
roots = list(map(generateTreebyLevelOrder, levelOrder))
for i in range(len(roots)):
    print('输入：{}\t结果：{}'.format(levelOrder[i], minDiffInBSTByDFS(roots[i])))
