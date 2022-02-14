# 5864. 游戏中弱角色的数量
# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [attacki, defensei] 表示游戏中第 i 个角色的属性。
# 如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，
# 如果认为角色 i 弱于 存在的另一个角色 j ，那么 attackj > attacki 且 defensej > defensei 。
# 返回 弱角色 的数量。
import collections


def numberOfWeakCharacters(properties: [[int]]) -> int:
    properties.sort(key=lambda x: (x[0], -x[1]))
    maxDefence = properties[-1][-1]
    result = 0
    for attack, defence in properties[::-1]:
        if defence < maxDefence:
            result += 1
        maxDefence = max(maxDefence, defence)
    return result


numberOfWeakCharacters([[5,5],[6,3],[3,6]])
numberOfWeakCharacters([[2,2],[3,3]])
numberOfWeakCharacters([[1,5],[10,4],[4,3]])
numberOfWeakCharacters([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]])



