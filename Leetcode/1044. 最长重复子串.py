"""
1044. 最长重复子串
给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。
"""
import random


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
        方法：二分查找 + Rabin-Karp编码
        记 s 的长度为 n。把问题分为两步：从 n - 1 到 1 由大至小遍历选取长度 L，判断 s 中是否有长度为 L 的重复子串。从大至小遍历的时候，
        第一次遇到的符合条件的L，即为最大的符合条件的 L ，记为 L_1， 重复的子串为 s_1.并且对于任意满足 L_0 \\leq L_1 的 L_0 也均符合条件，
        因为 s_1 的所有子串也是 s 的重复子串。而对于任意满足 L_2 > L_1 的 L_2，则均不符合条件。因此，可以用二分查找来查找 L_1.
        剩下的任务就是如何高效判断 s 中是否有长度为 L 的重复子串。可以使用 Rabin-Karp 算法对固定长度的字符串进行编码。当两个字符串编码相同时，
        则这两个字符串也相同。在 s 中 n - L + 1 个长度为 L 的子串中，有两个子串的编码相同时，则说明存在长度为 L 的重复子串。具体步骤如下：
        \\begin{enumerate}[1.]
        \\item 首先，我们需要对 s 的每个字符进行编码，得到一个数组 arr。因为本题中 s 仅包含小写字母，我们可以按照
        arr[i] = (int)s.charAt(i) - (int)'a', 将所有字母编码为 0 - 25 之间的数字。比如字符串 "abcde" 可以编码为数组 [0,1,2,3,4]。
        \\item 我们将子串看成一个 26 进制的数，它对应的 10 进制数就是它的编码。假设此时我们需要求长度为 3 的子串的编码。那么第一个子串 "abc"
        的编码就是 h_0 = 0 \\times 26^2 + 1 \\times 26^1 + 2 \\times 26^0 = 28.更一般地，设 c_i 为 s 的第 i 个字符编码后的数字，
        a (a \\geq 26) 为编码的进制，那么有
        h_0 = c_0 a^{L - 1} + c_1 a^{L - 2} + \\dots + c_{L - 1} a^1 = \\sum_{i = 0}^{L - 1}{c_i a^{L - 1 - i}}。
        \\item 上一步我们只求了第一个子串 "abc" 的编码。当我们要求第二个子串 "bcd" 的编码时，也可以按照上一步的方法求：
        h_1 = 1 \\times 26^2 + 2 \\times 26^1 + 3 \\times 26^0 = 731，但是这样时间复杂度是 O(L)。我们可以在 h_0 的基础上，
        更快地求出它的编码：h_1 = (h_0 - 0 \\times 26^2) \\times 26 + 3 \\times 26^0 = 731.更一般的表达式是：
        h_1 = (h_0 \\times a - c_0 \\times a^L) + c_{L + 1}。这样，我们只需要在常数时间内就可以根据上一个子串的编码求出下一个子串的编码。
        我们用哈希表 seen 来存储子串的编码。在求子串的编码时，如果某个子串的编码出现过，则表示长度为 L 的重复子串，否则，我们将当前编码放入
        seen 中。如果所有编码都不重复，则说明不存在长度为 L 的重复子串。
        \\item 还有一点要考虑的是，本题中 a^L 会非常大。一般的做法是需要对编码进行取模来防止溢出，模一般选取编码的信息量的平方的数量级。
        而取模则会带来哈希碰撞。本题中为了避免碰撞，我们是用双哈希，即用两套进制和模的组合，来对字符串进行编码。只有两种编码都相同时，我们才认为
        字符串相同。
        \\ 本题要求返回最长重复子串而不是最长重复子串长度。因此，当存在长度为 L 的子串时，我们的判断函数可以返回重复子串的起点。而不存在时，
        可以返回 -1 用作区分。
        """
        # 生成两个进制
        a1, a2 = random.randint(26, 100), random.randint(26, 100)
        # 生成两个模
        mod1, mod2 = random.randint(10 ** 9 + 7, 2 ** 31 - 1), random.randint(10 ** 9 + 7, 2 ** 31 - 1)
        n = len(s)
        # 先对所有字符进行编码
        arr = [ord(c) - ord('a') for c in s]
        # 二分查找的范围是 [1, n - 1]
        l, r = 1, n - 1
        length, start = 0, -1
        while l <= r:
            m = l + (r - l + 1) // 2
            index = self.check(arr, m, a1, a2, mod1, mod2)
            # 有重复子串，移动左边界
            if index != -1:
                l = m + 1
                length = m
                start = index
            # 无重复子串，移动右边界
            else:
                r = m - 1
        return s[start: start + length] if start != -1 else ''

    def check(self, arr, m, a1, a2, mod1, mod2):
        n = len(arr)
        aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
        h1, h2 = 0, 0
        for i in range(m):
            h1 = (h1 * a1 + arr[i]) % mod1
            h2 = (h2 * a2 + arr[i]) % mod2
        # 存储一个编码组合是否出现过
        seen = {(h1, h2)}
        for start in range(1, n - m + 1):
            h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
            h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + m - 1]) % mod2
            # 如果重复，返回字符串起点
            if (h1, h2) in seen:
                return start
            seen.add((h1, h2))
        # 没有重复，返回 -1
        return -1


a = Solution()
a.longestDupSubstring('aa')


