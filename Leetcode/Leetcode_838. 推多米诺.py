"""
838. 推多米诺
n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
返回表示最终状态的字符串。
"""
import collections


def pushDominoes(dominoes: str) -> str:
    flag = 0
    counter = 0
    result = ''
    for domino in dominoes:
        if domino == 'L':
            if flag == 1:
                result += 'R' * (counter // 2)
                result += '.' * (counter % 2)
                result += 'L' * (counter // 2)
            else:
                result += 'L' * counter
            result += 'L'
            flag = -1
            counter = 0
        elif domino == 'R':
            if flag == 1:
                result += 'R' * counter
            else:
                result += '.' * counter
            result += 'R'
            flag = 1
            counter = 0
        else:
            counter += 1
    if flag == 1:
        result += 'R' * counter
    else:
        result += '.' * counter
    return result


pushDominoes("RR.L")
pushDominoes(".L.R...LR..L..")


def pushDominoesBFS(dominoes: str) -> str:
    length = len(dominoes)
    q = collections.deque()
    times = [-1] * length
    forces = [[] for _ in range(length)]
    for idx, force in enumerate(dominoes):
        if force != '.':
            q.append(idx)
            times[idx] = 0
            forces[idx].append(force)
    result = ['.'] * length
    while q:
        index = q.popleft()
        if len(forces[index]) == 1:
            result[index] = force = forces[index][0]
            ni = index - 1 if force == 'L' else index + 1
            if 0 <= ni < length:
                t = times[index]
                if times[ni] == -1:
                    q.append(ni)
                    times[ni] = t + 1
                    forces[ni].append(force)
                elif times[ni] == t + 1:
                    forces[ni].append(force)
    return ''.join(result)


pushDominoesBFS("RR.L")
