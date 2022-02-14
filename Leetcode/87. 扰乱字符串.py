# 87. 扰乱字符串（以后再做）（不如先想想怎么产生所有的扰乱字符串）
# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
# 如果字符串的长度为 1 ，算法停止
# 如果字符串的长度 > 1 ，执行下述步骤：
# 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
# 随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
# 在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
# 给你两个 长度相等 的字符串 s1 和s2，判断s2是否是s1的扰乱字符串。如果是，返回 true ；否则，返回 false 。
import random


def createScrambleString(s1: str) -> [str]:
    result = []

    def subCreator(part: str, combination: list):
        if len(part) == 1:
            combination.append(part)
            if len(combination) == len(s1):
                result.append(combination.copy())
            return
        for i in range(1, len(part) - 1):
            subCreator(part[:i], combination.copy())
            subCreator(part[i:], combination)
        for i in range(1, len(part) - 1):
            subCreator(part[i:], combination.copy())
            subCreator(part[:i], combination)

    subCreator(s1, [])
    return result


s1 = "great"
createScrambleString(s1)
