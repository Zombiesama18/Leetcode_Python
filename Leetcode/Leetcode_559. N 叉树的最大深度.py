"""
559. N 叉树的最大深度
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
"""


def maxDepth(root) -> int:
    result = 0

    def helper(node, depth):
        nonlocal result
        if not node.children:
            result = max(result, depth)
        for child in node.children:
            helper(child, depth + 1)

    helper(root, 1)
    return result

