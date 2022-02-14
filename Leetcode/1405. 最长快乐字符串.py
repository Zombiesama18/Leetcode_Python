"""
1405. 最长快乐字符串
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。
"""
import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:
    pq = [[a, 'a'], [b, 'b'], [c, 'c']]
    result = ''
    while True:
        toBeContinue = False
        pq.sort(key=lambda x: -x[0])
        for i, (counter, char) in enumerate(pq):
            if counter > 0:
                if len(result) > 1 and result[-2] == result[-1] == char:
                    continue
                toBeContinue = True
                result += char
                pq[i][0] -= 1
                break
        if not toBeContinue:
            return result


longestDiverseString(1, 1, 7)
