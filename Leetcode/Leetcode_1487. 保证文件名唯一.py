"""
1487. 保证文件名唯一
给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，
其中 k 是能保证文件名唯一的 最小正整数 。
返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。
"""
import collections
import re
from typing import List


def getFolderNames(self, names: List[str]) -> List[str]:
    result = []
    counter = collections.defaultdict(int)

    for name in names:
        if name not in counter:
            counter[name] = 1
            result.append(name)
        else:
            number = counter[name]
            current_name = name + '(' + str(number) + ')'
            while current_name in counter:
                number += 1
                current_name = name + '(' + str(number) + ')'
            counter[name] = number + 1
            counter[current_name] = 1
            result.append(current_name)
    return result


