"""
6048. 必须拿起的最小连续卡牌数
给你一个整数数组 cards ，其中 cards[i] 表示第 i 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。
返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 -1 。
"""
from typing import List


def minimumCardPickup(cards: List[int]) -> int:
    result = float('INF')
    dictionary = dict()
    for i in range(len(cards)):
        if cards[i] in dictionary:
            result = min(result, i - dictionary[cards[i]])
        dictionary[cards[i]] = i
    return -1 if result == float('INF') else result + 1
