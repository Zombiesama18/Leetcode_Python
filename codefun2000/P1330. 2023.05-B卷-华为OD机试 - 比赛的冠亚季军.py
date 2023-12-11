"""
P1330. 2023.05-B卷-华为OD机试 - 比赛的冠亚季军

题目描述
有N(3≤N<10000)个运动员，他们的id为0到N−1,他们的实力由一组整数表示。他们之间进行比赛，需要决出冠亚军。比赛的规则是0号和1号比赛，
2号和3号比赛，以此类推，每一轮，相邻的运动员进行比赛，获胜的进入下一轮，实力值大的获胜，实力值相等的情况，id小的情况下获胜，轮空的直接进入下一轮。

输入描述
输入一行N个数字代表N的运动员的实力值(0≤实力值≤10000000000)。

输出描述
输出冠亚季军的id，用空格隔开。
"""


inputs = list(map(int, input().split()))
id_to_power = dict()
for i, power in enumerate(inputs):
    inputs[i] = i
    id_to_power[i] = power

while len(inputs) > 4:
    temp = []
    for i in range(0, len(inputs), 2):
        if id_to_power[inputs[i]] >= id_to_power[inputs[i + 1]]:
            temp.append(inputs[i])
        else:
            temp.append(inputs[i + 1])
    if len(inputs) % 2 == 1:
        temp.append(inputs[-1])
    inputs = temp

result = []
if len(inputs) == 4:
    win1, lose1 = sorted(inputs[0:2], key=lambda x: (-id_to_power[x], x))
    win2, lose2 = sorted(inputs[2:], key=lambda x: (-id_to_power[x], x))
    winwin1, winlose1 = sorted([win1, win2], key=lambda x: (-id_to_power[x], x))
    losewin2, loselose2 = sorted([lose1, lose2], key=lambda x: (-id_to_power[x], x))
    result = [winwin1, winlose1, losewin2]
else:
    win1, lose1 = sorted(inputs[0:2], key=lambda x: (-id_to_power[x], x))
    winwin1, winlose1 = sorted([win1, inputs[-1]], key=lambda x: (-id_to_power[x], x))
    result = [winwin1, winlose1, lose1]
print(' '.join(map(str, result)))
