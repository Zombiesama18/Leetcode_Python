import functools
from collections import deque


# 179. 最大数
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
def largestNumberPracticeofMergeSort(nums: [int]) -> str:
    def getMax(q1: deque, q2: deque):
        if len(q1) == 0:
            return q2.popleft()
        elif len(q2) == 0:
            return q1.popleft()
        else:
            if compareTo(q1[0], q2[0]):
                return q1.popleft()
            else:
                return q2.popleft()

    def compareTo(s1: str, s2: str):
        return s1 + s2 > s2 + s1

    dq = deque()
    for num in nums:
        dq.append(deque([str(num)]))
    while len(dq) != 1:
        q1 = dq.popleft()
        q2 = dq.popleft()
        temp = deque()
        while len(q1) != 0 or len(q2) != 0:
            temp.append(getMax(q1, q2))
        dq.append(temp)
    result = ''.join(dq.pop())
    if result[0] == '0':
        result = '0'
    return result


numss = [[34323,3432], [3,30,34,5,9], [10,2], [1], [10]]
for num in numss:
    print('输入：{}\t结果：{}'.format(num, largestNumberPracticeofMergeSort(num)))


# Python3中list的sort()没有了cmp=，只有key=，但是key=只能传一个参数
# 解决方法：使用functools.cmp_to_key来解决
def largestNumberBySetCompareMode(nums: [int]) -> str:
    numsString = list(map(str, nums))
    compareMode = lambda x, y: 1 if x + y < y + x else -1
    numsString.sort(key=functools.cmp_to_key(compareMode))
    result = ''.join(numsString)
    if result[0] == '0':
        result = '0'
    return result


numss = [[3,30,34,5,9], [10,2], [1], [10]]
for num in numss:
    print('输入：{}\t结果：{}'.format(num, largestNumberBySetCompareMode(num)))

