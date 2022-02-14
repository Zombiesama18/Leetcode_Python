# 1734. 解码异或后的排列（需要复习）
# 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
# 它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。
# 比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
# 给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。
# 数学问题，解法：
# perm的第一个元素是最容易得到的，
# 由于perm是前n个正整数的排列，所以数组perm的全部元素的异或运算结果即为从1到n的全部正整数的异或运算结果，用total表示数组perm的全部元素的异或运算结果，则有：
# total = 1 ^ 2 ^ ... ^ n = perm[0] ^ perm[1] ^ ... ^ perm[n-1]
# 由于n是奇数，除了perm[0]以外，数组perm还有n-1个其他元素，n-1是偶数，又由于数组encoded的每个元素都是数组perm的两个元素异或运算的结果，
# 因此数组encoded中存在(n-1)/2个元素，这些元素的异或运算结果为数组perm除了perm[0]以外的全部元素的异或运算结果。
# 即，数组encoded的所有下标为奇数的元素的异或运算结果即为数组perm除了perm[0]以外的全部元素的异或运算结果，用odd表示数组encoded的所有下标为奇数的元素的异或运算结果：
# odd = encoded[1] ^ encoded[3] ^ ... ^ encoded[n-2] = perm[1] ^ perm[2] ^ ...perm[n]
# 则可计算得到perm[0]的值，perm[0] = (perm[0] ^ perm[n]) ^ (perm[1] ^ ... ^ perm[n]) = total ^ odd
from functools import reduce
from operator import xor


def decode(encoded: [int]) -> [int]:
    length = len(encoded)
    result = [0] * (length + 1)
    totalXOR = reduce(xor, range(1, length + 2))
    # totalXOR = 1
    #
    # for i in range(2, length + 2):
    #     totalXOR = totalXOR ^ i
    oddXOR = reduce(xor, encoded[1:length:2])
    # oddXOR = encoded[1]
    # for i in range(3, length, 2):
    #     oddXOR = oddXOR ^ encoded[i]
    result[0] = totalXOR ^ oddXOR
    for i in range(1, length + 1):
        result[i] = result[i - 1] ^ encoded[i - 1]
    return result


decode([3,1])
decode([6,5,4,6])
decode([7,5,6,11,14,15,11,6])
