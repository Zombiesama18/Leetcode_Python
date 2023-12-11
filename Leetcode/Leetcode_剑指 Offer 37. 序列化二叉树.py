from collections import deque
from libraries.utils import TreeNode


# 剑指 Offer 37. 序列化二叉树
# 请实现两个函数，分别用来序列化和反序列化二叉树。
# 你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        return self.serializeHelper(root, '')

    def serializeHelper(self, node, result):
        if node is None:
            result += 'None,'
        else:
            result += '{},'.format(node.val)
            result = self.serializeHelper(node.left, result)
            result = self.serializeHelper(node.right, result)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        elements = data.split(',')
        return self.deserializeHelper(elements)

    def deserializeHelper(self, elements: list):
        if elements[0] == "None":
            elements.pop(0)
            return None
        root = TreeNode(elements[0])
        elements.pop(0)
        root.left = self.deserializeHelper(elements)
        root.right = self.deserializeHelper(elements)
        return root

