"""
735. 行星碰撞
给定一个整数数组 asteroids，表示在同一行的行星。
对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。
两颗移动方向相同的行星，永远不会发生碰撞。
"""
from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        alive = True
        while alive and asteroid < 0 and stack and stack[-1] > 0:
            alive = -asteroid > stack[-1]
            if -asteroid >= stack[-1]:
                stack.pop(-1)
        if alive:
            stack.append(asteroid)
    return stack


asteroidCollision([1,-2,-2,-2])
