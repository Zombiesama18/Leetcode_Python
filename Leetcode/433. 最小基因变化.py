"""
433. 最小基因变化
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。
给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。
如果无法完成此基因变化，返回 -1 。
注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
"""
import collections
from typing import List


def minMutation(start: str, end: str, bank: List[str]) -> int:
    q = collections.deque([(start, 0)])
    bank = set(bank)
    if start == end:
        return 0
    if end not in bank:
        return -1
    while q:
        current, step = q.popleft()
        for i, x in enumerate(current):
            for y in 'AGCT':
                if y != x:
                    nextSeq = current[:i] + y + current[i + 1:]
                    if nextSeq in bank:
                        if nextSeq == end:
                            return step + 1
                        bank.remove(nextSeq)
                        q.append((nextSeq, step + 1))
    return -1

