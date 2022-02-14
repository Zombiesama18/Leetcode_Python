# 5911. 模拟行走机器人 II
# 给你一个在 XY 平面上的 width x height 的网格图，左下角 的格子为 (0, 0) ，右上角 的格子为 (width - 1, height - 1) 。
# 网格图中相邻格子为四个基本方向之一（"North"，"East"，"South" 和 "West"）。一个机器人 初始 在格子 (0, 0) ，方向为 "East" 。
# 机器人可以根据指令移动指定的 步数 。每一步，它可以执行以下操作。
# 沿着当前方向尝试 往前一步 。
# 如果机器人下一步将到达的格子 超出了边界 ，机器人会 逆时针 转 90 度，然后再尝试往前一步。
# 如果机器人完成了指令要求的移动步数，它将停止移动并等待下一个指令。
# 请你实现 Robot 类：
# Robot(int width, int height) 初始化一个 width x height 的网格图，机器人初始在 (0, 0) ，方向朝 "East" 。
# void move(int num) 给机器人下达前进 num 步的指令。
# int[] getPos() 返回机器人当前所处的格子位置，用一个长度为 2 的数组 [x, y] 表示。
# String getDir() 返回当前机器人的朝向，为 "North" ，"East" ，"South" 或者 "West" 。
class Robot:

    def __init__(self, width: int, height: int):
        self.position = 0
        self.width = width
        self.height = height
        self.one_edge = width - 1
        self.two_edges = height + width - 2
        self.three_edges = width * 2 + height - 3
        self.circle = 2 * (width + height - 2)
        self.direction_flag = True

    def move(self, num: int) -> None:
        self.position = (self.position + num) % self.circle
        self.direction_flag = False

    def getPos(self) -> [int]:
        if 0 <= self.position <= (self.width - 1):
            return [self.position, 0]
        if self.position <= self.height + self.width - 2:
            return [self.width - 1, self.position - self.width + 1]
        if self.position <= 2 * self.width + self.height - 3:
            return [2 * self.width + self.height - 3 - self.position, self.height - 1]
        return [0, self.circle - self.position]

    def getDir(self) -> str:
        if self.direction_flag and self.position == 0:
            return 'East'
        else:
            if 0 < self.position <= self.width - 1:
                return 'East'
            if self.width - 1 < self.position <= self.width + self.height - 2:
                return 'North'
            if self.width + self.height - 2 < self.position <= 2 * self.width + self.height - 3:
                return 'West'
            return 'South'


robot = Robot(3, 3)
robot.move(26)
robot.move(34)
robot.move(30)
robot.move(45)
robot.move(25)
robot.getDir()

