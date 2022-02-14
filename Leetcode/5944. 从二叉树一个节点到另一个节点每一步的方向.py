"""
5944. 从二叉树一个节点到另一个节点每一步的方向
给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数 startValue ，
表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。
请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向：
'L' 表示从一个节点前往它的 左孩子 节点。
'R' 表示从一个节点前往它的 右孩子 节点。
'U' 表示从一个节点前往它的 父 节点。
请你返回从 s 到 t 最短路径 每一步的方向。
"""
from libraries.utils import generateTreebyLevelOrder


def getDirections(root, startValue: int, destValue: int) -> str:
    def find(node, target, path):
        if not node:
            return False
        if node.val == target:
            return True
        if find(node.left, target, path):
            path.append('L')
            return True
        if find(node.right, target, path):
            path.append('R')
            return True
        return False

    start_path, dest_path = [], []
    find(root, startValue, start_path)
    find(root, destValue, dest_path)
    start_path, dest_path = list(reversed(start_path)), list(reversed(dest_path))
    while len(start_path) > 0 and len(dest_path) > 0 and start_path[0] == dest_path[0]:
        start_path.pop(0)
        dest_path.pop(0)
    return 'U' * len(start_path) + ''.join(dest_path)


root = generateTreebyLevelOrder([5,1,2,3,None,6,4])
getDirections(root, 3, 6)




