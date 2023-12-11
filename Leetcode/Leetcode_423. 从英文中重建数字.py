"""
423. 从英文中重建数字
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
"""
import collections


def originalDigits(s: str) -> str:
    first_list = ['zero', 'two', 'four', 'six', 'eight']
    first_query = ['z', 'w', 'u', 'x', 'g']
    second_list = ['one', 'three', 'seven']
    second_query = ['o', 'r', 's']
    third_list = ['five', 'nine']
    third_query = ['v', 'i']
    word_to_number = {'zero': 0, 'two': 2, 'four': 4, 'six': 6, 'eight': 8, 'one': 1, 'three': 3, 'seven': 7, 'five': 5,
                      'nine': 9}
    s_dict = collections.Counter(s)
    result = []
    for i in range(len(first_list)):
        if s_dict[first_query[i]] != 0:
            number = s_dict[first_query[i]]
            result.extend([word_to_number[first_list[i]]] * number)
            for char in first_list[i]:
                s_dict[char] -= number
    for i in range(len(second_list)):
        if s_dict[second_query[i]] != 0:
            number = s_dict[second_query[i]]
            result.extend([word_to_number[second_list[i]]] * number)
            for char in second_list[i]:
                s_dict[char] -= number
    if s_dict[third_query[0]] != 0:
        number = s_dict[third_query[0]]
        result.extend([word_to_number[third_list[0]]] * number)
        for char in third_list[0]:
            s_dict[char] -= number
    if s_dict[third_query[1]] != 0:
        result.extend([word_to_number[third_list[1]]] * s_dict[third_query[1]])
    result.sort()
    result = list(map(str, result))
    return ''.join(result)


originalDigits("owoztneoer")
originalDigits("fviefuro")
originalDigits("nnei")

