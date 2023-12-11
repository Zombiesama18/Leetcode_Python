"""
5217. 将杂乱无章的数字排序
给你一个下标从 0 开始的整数数组 mapping ，它表示一个十进制数的映射规则，mapping[i] = j 表示这个规则下将数位 i 映射为数位 j 。
一个整数 映射后的值 为将原数字每一个数位 i （0 <= i <= 9）映射为 mapping[i] 。
另外给你一个整数数组 nums ，请你将数组 nums 中每个数按照它们映射后对应数字非递减顺序排序后返回。
注意：
如果两个数字映射后对应的数字大小相同，则将它们按照输入中的 相对顺序 排序。
nums 中的元素只有在排序的时候需要按照映射后的值进行比较，返回的值应该是输入的元素本身。
"""
import collections
from typing import List


def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
    dictionary = {i: num for i, num in enumerate(mapping)}
    dictionary2 = collections.defaultdict(list)
    convertedNumbers = []
    for num in nums:
        rawNumber = num
        stack = []
        if num == 0:
            stack.append(0)
        while num != 0:
            stack.append(num % 10)
            num //= 10
        newNumber = 0
        while stack:
            newNumber *= 10
            newNumber += dictionary[stack.pop(-1)]
        dictionary2[newNumber].append(rawNumber)
        convertedNumbers.append(newNumber)
    convertedNumbers.sort()
    result = []
    for num in convertedNumbers:
        for resultNumber in dictionary2[num]:
            result.append(resultNumber)
        dictionary2.pop(num)
    return result


sortJumbled([9,8,7,6,5,4,3,2,1,0], [0,1,2,3,4,5,6,7,8,9])


def sortJumbledSimpler(mapping: List[int], nums: List[int]) -> List[int]:
    table = str.maketrans('0123456789', ''.join(map(str, mapping)))
    return sorted(nums, key=lambda x: int(str(x).translate(table)))



