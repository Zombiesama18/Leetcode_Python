"""
449. 序列化和反序列化二叉搜索树
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
编码的字符串应尽可能紧凑。
"""
from libraries.utils import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        result = []

        def postOrderTraverse(node: TreeNode):
            if not node:
                return
            postOrderTraverse(node.left)
            postOrderTraverse(node.right)
            result.append(node.val)
            return

        postOrderTraverse(root)
        return ' '.join(map(str, result))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        numbers = list(map(int, data.split()))

        def construct(lower, upper):
            if not numbers or numbers[-1] < lower or numbers[-1] > upper:
                return None
            value = numbers.pop(-1)
            node = TreeNode(value)
            node.right = construct(value, upper)
            node.left = construct(lower, value)
            return node

        return construct(float('-inf'), float('inf'))




