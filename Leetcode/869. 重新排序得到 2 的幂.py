# 869. 重新排序得到 2 的幂
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
import collections


def reorderedPowerOf2(n: int) -> bool:
    def isPowerOf2(num: int):
        return (num & (num - 1)) == 0

    nums = sorted(list(str(n)))
    length = len(nums)
    traversed = [False] * length

    def DFS(counter: int, num: int):
        if counter == length:
            return isPowerOf2(num)
        for i, char in enumerate(nums):
            if (num == 0 and char == '0') or traversed[i] or (i > 0 and not traversed[i - 1] and char == nums[i - 1]):
                continue
            traversed[i] = True
            if DFS(counter + 1, num * 10 + ord(char) - ord('0')):
                return True
            traversed[i] = False
        return False

    return DFS(0, 0)


def reorderedPowerOf2V2(n: int) -> bool:
    possibleDict = collections.defaultdict(list)
    number = 1
    while len(str(number)) < 10:
        possibleDict[len(str(number))].append(sorted(str(number)))
        number *= 2
    n = sorted(str(n))
    return n in possibleDict[len(n)]


reorderedPowerOf2V2(46)
reorderedPowerOf2V2(635824465)
