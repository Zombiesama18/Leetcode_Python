# 1104. 二叉树寻路
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
import math


def pathInZigZagTree(label: int) -> [int]:
    column = int(math.floor(math.log2(label)))
    result = []
    while column > 0:
        result.insert(0, label)
        if column % 2 == 1:
            base = int(math.pow(2, column + 1) - 1)
            index = base - label
            base = int(math.pow(2, column - 1))
            label = base + index // 2
        else:
            base = int(math.pow(2, column))
            index = label - base
            base -= 1
            label = base - index // 2
        column -= 1
    result.insert(0, 1)
    return result


pathInZigZagTree(14)
pathInZigZagTree(26)



