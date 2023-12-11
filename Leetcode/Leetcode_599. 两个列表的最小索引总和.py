"""
599. 两个列表的最小索引总和
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。
"""
from typing import List


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    list1Dict = {value: index for index, value in enumerate(list1)}
    list2Dict = {value: index for index, value in enumerate(list2)}
    result = []
    indexSum = float('INF')
    for value in list1Dict:
        if value in list2Dict:
            if list1Dict[value] + list2Dict[value] < indexSum:
                result = [value]
                indexSum = list1Dict[value] + list2Dict[value]
            elif list1Dict[value] + list2Dict[value] == indexSum:
                result.append(value)
    return result
