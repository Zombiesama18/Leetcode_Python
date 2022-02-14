from libraries.utils import TreeNode, generateTreebyLevelOrder, inorderTravesal

# 173. 二叉搜索树迭代器
# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于
# BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
# 你可以假设next()调用总是有效的，也就是说，当调用 next()时，BST 的中序遍历中至少存在一个下一个数字。
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.inOrder = list()
        self.inOrderTraversal(root)
        self.index = 0
        self.length = len(self.inOrder)

    def inOrderTraversal(self, node):
        if not node:
            return
        self.inOrderTraversal(node.left)
        self.inOrder.append(node.val)
        self.inOrderTraversal(node.right)
        return

    def next(self) -> int:
        temp = self.inOrder[self.index]
        self.index += 1
        return temp

    def hasNext(self) -> bool:
        return self.index < self.length


levelOrder = [7, 3, 15, None, None, 9, 20]
root = generateTreebyLevelOrder(levelOrder)
inorderTravesal(root)
