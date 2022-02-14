# 5908. 统计最高分的节点数目
# 给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，
# 其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。
# 一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，
# 剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。
# 请你返回有 最高得分 节点的 数目 。
import collections


def countHighestScoreNodes(parents: [int]) -> int:
    childrenDict = collections.defaultdict(list)
    for i in range(1, len(parents)):
        childrenDict[parents[i]].append(i)
    scoreDict = dict()

    def computerNumber(node: int):
        counter = 1
        for child in childrenDict[node]:
            counter += computerNumber(child)
        scoreDict[node] = counter
        return counter

    computerNumber(0)
    length = len(parents)
    result = 0
    maxLength = float('-INF')
    for i in range(length):
        tempCounter = 1
        if parents[i] == -1:
            for child in childrenDict[i]:
                tempCounter *= scoreDict[child]
        elif not childrenDict[i]:
            tempCounter = length - 1
        else:
            temp = 0
            for child in childrenDict[i]:
                tempCounter *= scoreDict[child]
                temp += scoreDict[child]
            tempCounter *= length - 1 - temp
        if tempCounter > maxLength:
            maxLength = tempCounter
            result = 1
        elif tempCounter == maxLength:
            result += 1
    return result


countHighestScoreNodes([-1,2,0,2,0])
countHighestScoreNodes([-1,2,0])
countHighestScoreNodes([-1,3,3,5,7,6,0,0])
countHighestScoreNodes([-1,0,0,1,1])
