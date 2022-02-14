"""
730. 机器人跳跃问题
机器人正在玩一个古老的基于 DOS 的游戏。
游戏中有 N+1 座建筑——从 0 到 N 编号，从左到右排列。
编号为 0 的建筑高度为 0 个单位，编号为 i 的建筑高度为 H(i) 个单位。
起初，机器人在编号为 0 的建筑处。
每一步，它跳到下一个（右边）建筑。
假设机器人在第 k 个建筑，且它现在的能量值是 E，下一步它将跳到第 k+1 个建筑。
如果 H(k+1)>E，那么机器人就失去 H(k+1)−E 的能量值，否则它将得到 E−H(k+1) 的能量值。
游戏目标是到达第 N 个建筑，在这个过程中能量值不能为负数个单位。
现在的问题是机器人至少以多少能量值开始游戏，才可以保证成功完成游戏？
"""


def solution(number, heights):
    result = 0
    heights = heights
    for i in range(len(heights) - 1, -1, -1):
        result = (result + heights[i] + 1) // 2
    return result


solution(5, [3, 4, 3, 2, 4])
solution(3, [4, 4, 4])
solution(3, [1, 6, 4])

