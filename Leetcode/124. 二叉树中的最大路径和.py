from libraries import Tree


# 124. 二叉树中的最大路径和
# 给定一个非空二叉树，返回其最大路径和。
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
def maxPathSum(root):
    values = []
    nodelist = []

    def get_values(now):
        values.append(now.val)
        nodelist.append(now)
        if not now.left and not now.right:
            return
        if now.left:
            get_values(now.left)
        if now.right:
            get_values(now.right)
        return

    def is_connected(now, nums):
        nums.remove(now.val)
        if not nums:
            return True
        if not now.left and not now.right:
            return False
        if now.left:
            if now.left.val in nums:
                flag = is_connected(now.left, nums)
            else:
                return False
        if now.right:
            if now.right.val in nums:
                flag = is_connected(now.right, nums)
            else:
                return flag
        return flag

    get_values(root)
    seqs = []
    for i in range(len(values)):
        for j in range(i + 1, len(values) + 1):
            if len(values[i:j]) > 1:
                if is_connected(nodelist[i], values[i:j]):
                    seqs.append(values[i:j])
            else:
                seqs.append(values[i:j])
    sum_seq = []
    for i in range(len(seqs)):
        sum_seq.append(sum(seqs[i]))
    return max(sum_seq)


tree = Tree.Tree([-10, 9, 20, None, None, 15, 7])
maxPathSum(tree.root)
