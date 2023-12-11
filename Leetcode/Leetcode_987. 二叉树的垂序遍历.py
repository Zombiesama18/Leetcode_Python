# 987. 二叉树的垂序遍历
# 给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。
# 对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。
# 二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。
# 返回二叉树的 垂序遍历 序列。
import collections
import queue

from libraries.utils import TreeNode


def verticalTraversal(root: TreeNode) -> [[int]]:
    nodeDict = {}
    nodeQueue = collections.deque([(root, 0)])
    while nodeQueue:
        currentNode, currentCol = nodeQueue.popleft()
        if currentCol in nodeDict:
            nodeDict[currentCol].append(currentNode.val)
        else:
            nodeDict[currentCol] = [currentNode.val]
        if currentNode.left:
            nodeQueue.append((currentNode.left, currentCol - 1))
        if currentNode.right:
            nodeQueue.append((currentNode.right, currentCol + 1))
    nodeCols = list(nodeDict.keys())
    nodeCols.sort()
    result = []
    for col in nodeCols:
        result.append(nodeDict[col])
    return result




