"""
997. 找到小镇的法官
在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。
如果小镇的法官真的存在，那么：
小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足条件 1 和条件 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。
如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。
"""
import collections
from typing import List


def findJudge(n: int, trust: List[List[int]]) -> int:
    to_trust, from_trust = [set() for _ in range(n + 1)], [set() for _ in range(n + 1)]
    for source, to in trust:
        to_trust[source].add(to)
        from_trust[to].add(source)
    for i in range(1, n + 1):
        if len(from_trust[i]) == n - 1 and len(to_trust[i]) == 0:
            return i
    return -1


def findJudgeVersion2(n: int, trust: List[List[int]]) -> int:
    in_degrees = collections.Counter(to for _, to in trust)
    out_degrees = collections.Counter(source for source, _ in trust)
    for i in range(1, n + 1):
        if in_degrees[i] == n - 1 and out_degrees[i] == 0:
            return i
    return -1


