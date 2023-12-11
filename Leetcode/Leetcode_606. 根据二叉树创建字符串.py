"""
606. 根据二叉树创建字符串
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
"""
from typing import Optional

from libraries.utils import TreeNode


def tree2str(root: Optional[TreeNode]) -> str:
    def search(node):
        if not node:
            return ''
        temp = str(node.val)
        if node.left or node.right:
            temp += '('
            temp += search(node.left)
            temp += ')'
            if node.right:
                temp += '('
                temp += search(node.right)
                temp += ')'
        return temp

    return search(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
tree2str(root)

