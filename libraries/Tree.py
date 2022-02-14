class Tree:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def __init__(self, levelOrder):
        self.root = self.generateTreebyLevelOrder(levelOrder)

    def generateTreebyLevelOrder(self, levelOrder):
        length = len(levelOrder)
        nodeList = list()
        for item in levelOrder:
            if not item:
                nodeList.append(None)
            else:
                nodeList.append(self.TreeNode(item))
        for i in range(length):
            if 2 * i + 2 > length - 1:
                break
            nodeList[i].left = nodeList[2 * i + 1]
            nodeList[i].right = nodeList[2 * i + 2]
        return nodeList[0]

    def inorderTravesal(self):
        result = []

        def subInorderTraversal(node):
            if not node:
                return
            subInorderTraversal(node.left)
            result.append(node.val)
            subInorderTraversal(node.right)
            return

        subInorderTraversal(self.root)
        return result

    def preorderTraversal(self):
        result = []

        def subPreorderTraversal(node):
            if not node:
                return
            result.append(node.val)
            subPreorderTraversal(node.left)
            subPreorderTraversal(node.right)
            return

        subPreorderTraversal(self.root)
        return result

    def postorderTraversal(self):
        result = []

        def subPostorderTraversal(node):
            if not node:
                return
            subPostorderTraversal(node.left)
            subPostorderTraversal(node.right)
            result.append(node.val)
            return

        subPostorderTraversal(self.root)
        return result



