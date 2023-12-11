"""题目内容
AI识别到面板上有N个指示灯，灯大小一样，任意两个之间无重叠。
由于AI识别误差，每次识别到的指示灯位置可能有差异，
以4个坐标值描述AI识别的指示灯的大小和位置(左上角x1,y1)，右下角(x2,y2)
请输出先行后列排序的指示灯的编号，排序规则:

1.每次在尚未排序的灯中挑选最高的灯作为的基准灯，
2.找出和基准灯属于同一行所有的灯进行排序。
两人灯高低偏差不超过灯半径算同一行(即两个灯坐标的差≤灯高度的一半)。

输入描述
第一行为N，表示灯的个数 接下来N行，每行为1个灯的坐标信息，格式为:
编号x_1 y_1 x_2 y_2

输出描述
排序后的编号列表，编号之间以空格分隔

用例
输入
5
1 0 0 2 2
2 6 1 8 3
3 3 2 5 4
5 5 4 7 6
4 0 4 2 6

输出
1 2 3 4 5
"""

N = int(input())
lights =[]
for _ in range(N):
    lights.append(list(map(int, input().split())))

h = (lights[0][-1] - lights[0][2]) / 2

lights.sort(key=lambda x: x[2])
result = []
while lights:
    temp = [lights.pop(0)]
    while lights[0][2] - temp[0][2] <= h:
        temp.append(lights.pop(0))
        if not lights:
            break
    temp.sort(key=lambda x: x[1])
    for item in temp:
        result.append(item[0])
print(' '.join(map(str, result)))

