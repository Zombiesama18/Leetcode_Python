"""
874. 模拟行走机器人

机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：
-2 ：向左转 90 度
-1 ：向右转 90 度
1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）
"""
import collections
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0, 0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        obstacle_x_dict = collections.defaultdict(list)
        obstacle_y_dict = collections.defaultdict(list)
        result = 0
        for x, y in obstacles:
            obstacle_x_dict[x].append(y)
            obstacle_y_dict[y].append(x)
        for k, v in obstacle_x_dict.items():
            obstacle_x_dict[k] = list(sorted(v))
        for k, v in obstacle_y_dict.items():
            obstacle_y_dict[k] = list(sorted(v))
        for command in commands:
            if command == -1:
                direction_index = (direction_index + 1) % 4
            elif command == -2:
                direction_index = (direction_index - 1) % 4
            else:
                if direction_index % 2 == 0:
                    target_pos = [pos[0], pos[1] + directions[direction_index][1] * command]
                    if direction_index == 0:
                        for obstacle_y in obstacle_x_dict[pos[0]]:
                            if pos[1] < obstacle_y <= target_pos[1]:
                                target_pos[1] = obstacle_y - 1
                                break
                    elif direction_index == 2:
                        for obstacle_y in reversed(obstacle_x_dict[pos[0]]):
                            if target_pos[1] <= obstacle_y < pos[1]:
                                target_pos[1] = obstacle_y + 1
                                break
                elif direction_index % 2 == 1:
                    target_pos = [pos[0] + directions[direction_index][0] * command, pos[1]]
                    if direction_index == 1:
                        for obstacle_x in obstacle_y_dict[pos[1]]:
                            if pos[0] < obstacle_x <= target_pos[0]:
                                target_pos[0] = obstacle_x - 1
                                break
                    elif direction_index == 3:
                        for obstacle_x in reversed(obstacle_y_dict[pos[1]]):
                            if target_pos[0] <= obstacle_x < pos[0]:
                                target_pos[0] = obstacle_x + 1
                                break
                result = max(result, target_pos[0] ** 2 + target_pos[1] ** 2)
                pos = target_pos
        return result


Solution().robotSim(commands = [4,-1,3], obstacles = [])
Solution().robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]])
Solution().robotSim([2,-1,8,-1,6], [[1,5],[-5,-5],[0,4],[-1,-1],[4,5],[-5,-3],[-2,1],[-2,-5],[0,5],[0,-1]])
Solution().robotSim([-2,3,-1,-2,4], [[-2,2],[4,-3],[2,3],[-3,-2],[-2,-4],[0,-4],[2,2],[3,-2],[2,-5],[2,1]])
